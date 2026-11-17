
# MobileCare AI
# Semantic Natural Language Matching Engine

import math
import streamlit as st
from fastembed import TextEmbedding


# --------------------------------------------------
# MODEL CONFIGURATION
# --------------------------------------------------

MODEL_NAME = (
    "sentence-transformers/"
    "paraphrase-multilingual-MiniLM-L12-v2"
)


# --------------------------------------------------
# LOAD MODEL ONLY ONCE
# --------------------------------------------------

@st.cache_resource(show_spinner="Loading language model...")
def load_embedding_model():

    return TextEmbedding(
        model_name=MODEL_NAME
    )


# --------------------------------------------------
# PREPARE ASSERTION TEXT
# --------------------------------------------------

def prepare_assertion_text(assertion):

    fact = assertion.get("fact", "")

    description = assertion.get(
        "description", ""
    )

    category = assertion.get(
        "category", ""
    )

    keywords = assertion.get(
        "keywords", []
    )

    keyword_text = " ".join(keywords)

    return (
        f"Mobile problem: {fact.replace('_', ' ')}. "
        f"Description: {description}. "
        f"Category: {category}. "
        f"Related expressions: {keyword_text}"
    )


# --------------------------------------------------
# GENERATE AND CACHE FACT EMBEDDINGS
# --------------------------------------------------

@st.cache_data(show_spinner=False)
def create_fact_embeddings(assertion_texts):

    model = load_embedding_model()

    embeddings = model.embed(
        list(assertion_texts)
    )

    return tuple(
        tuple(float(value) for value in vector)
        for vector in embeddings
    )


# --------------------------------------------------
# COSINE SIMILARITY
# --------------------------------------------------

def cosine_similarity(vector_a, vector_b):

    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (
        magnitude_a * magnitude_b
    )


# --------------------------------------------------
# SEMANTIC FACT SEARCH
# --------------------------------------------------

def search_similar_facts(
    user_question,
    assertions,
    top_k=5,
    min_score=0.35
):

    if not user_question.strip():
        return []

    if not assertions:
        return []

    model = load_embedding_model()

    # Prepare knowledge base descriptions

    assertion_texts = tuple(
        prepare_assertion_text(assertion)
        for assertion in assertions
    )

    # Get cached fact embeddings

    fact_embeddings = create_fact_embeddings(
        assertion_texts
    )

    # Convert user question into embedding

    query_vector = list(
        model.embed([user_question])
    )[0]

    query_vector = [
        float(value)
        for value in query_vector
    ]

    # Compare question with every assertion

    results = []

    for assertion, fact_vector in zip(
        assertions,
        fact_embeddings
    ):

        score = cosine_similarity(
            query_vector,
            fact_vector
        )

        if score >= min_score:

            results.append({
                "fact": assertion["fact"],
                "description": assertion.get(
                    "description", ""
                ),
                "score": round(score, 4)
            })

    # Highest similarity first

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]

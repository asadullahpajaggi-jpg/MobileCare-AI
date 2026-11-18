"""Conservative rule-based NLP utilities for MobileCare AI.

This module extracts only explicit, positively stated knowledge-base facts.
It does not use semantic similarity as proof of a fact.
"""

import re


NEGATION_WORDS = {
    "not", "no", "never", "without", "cannot", "cant", "wont",
    "isnt", "arent", "doesnt", "dont", "didnt", "wasnt", "werent",
}

CONTRACTIONS = {
    "can't": "can not",
    "cannot": "can not",
    "won't": "will not",
    "isn't": "is not",
    "aren't": "are not",
    "doesn't": "does not",
    "don't": "do not",
    "didn't": "did not",
    "wasn't": "was not",
    "weren't": "were not",
}

# Carefully selected wording variants for common Android support issues.
# These are retrieval aliases, not extra facts or diagnoses.
FACT_ALIASES = {
    "battery_drains_fast": [
        "battery drains quickly", "battery dies quickly",
        "battery runs out fast", "battery runs out quickly",
    ],
    "phone_not_charging": [
        "phone will not charge", "phone won't charge",
        "cannot charge phone", "phone is not charging",
    ],
    "phone_overheating": [
        "phone gets hot", "phone is getting hot",
        "mobile gets hot", "device is overheating",
        "phone heats up", "mobile heats up", "overheating",
    ],
    "wifi_not_working": [
        "wi fi not working", "wifi will not connect",
        "wifi won't connect", "cannot connect to wifi",
        "can't connect to wifi", "wifi is not connecting",
    ],
    "wifi_connected_no_internet": [
        "wifi connected but no internet",
        "connected to wifi no internet",
        "wifi has no internet access",
    ],
    "mobile_data_not_working": [
        "mobile internet not working", "cellular data not working",
        "mobile data has no internet",
    ],
    "no_network_signal": [
        "no signal", "no mobile signal", "network signal missing",
    ],
    "sim_not_detected": [
        "phone cannot detect sim", "sim is not detected",
        "no sim card detected", "sim card not recognized",
    ],
    "phone_slow": [
        "phone is lagging", "mobile is lagging",
        "phone responds slowly", "mobile responds slowly",
    ],
    "apps_crashing": [
        "apps keep closing", "applications keep closing",
        "app keeps stopping",
    ],
}


def _expand_contractions(text):
    """Expand common English contractions before tokenization."""
    value = str(text or "").lower()
    for contraction, expanded in CONTRACTIONS.items():
        value = re.sub(
            r"\b" + re.escape(contraction) + r"\b",
            expanded,
            value,
        )
    return value


def _normalize_word(word):
    """Apply small, conservative English inflection normalization."""
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"

    if len(word) > 5 and word.endswith("ing"):
        stem = word[:-3]
        if len(stem) > 2 and stem[-1] == stem[-2]:
            stem = stem[:-1]
        # Preserve common silent-e verb forms.
        if stem in {"charg", "us", "mak", "tak", "writ"}:
            stem += "e"
        return stem

    if len(word) > 4 and word.endswith("ed"):
        stem = word[:-2]
        if len(stem) > 2 and stem[-1] == stem[-2]:
            stem = stem[:-1]
        if stem in {"charg", "us", "mov"}:
            stem += "e"
        return stem

    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]

    return word


def normalize_tokens(text):
    """Tokenize text and normalize common inflected word forms."""
    expanded = _expand_contractions(text)
    words = re.findall(r"[a-z0-9]+", expanded)
    normalized = [_normalize_word(word) for word in words]
    return normalized


def _phrase_positions(user_words, keyword):
    """Find keyword words in order, allowing a few natural filler words."""
    phrase_words = normalize_tokens(keyword)
    if not phrase_words:
        return None

    # Avoid matching very short generic one-word terms such as 'hot' or 'app'.
    if len(phrase_words) == 1 and len(phrase_words[0]) < 5:
        return None

    for start, token in enumerate(user_words):
        if token != phrase_words[0]:
            continue

        positions = [start]
        cursor = start + 1

        for phrase_word in phrase_words[1:]:
            found = None
            # Allow up to two intervening words, e.g. 'battery is draining'.
            for index in range(cursor, min(cursor + 3, len(user_words))):
                if user_words[index] == phrase_word:
                    found = index
                    break
            if found is None:
                break
            positions.append(found)
            cursor = found + 1

        if len(positions) == len(phrase_words):
            return positions

    return None


def _is_negated(user_words, positions, keyword):
    """Check negation around a match without rejecting negation in its keyword."""
    if not positions:
        return False

    keyword_words = set(normalize_tokens(keyword))
    start = min(positions)
    end = max(positions)

    # A preceding negation changes polarity unless it is itself part of
    # the matched keyword (e.g. 'not charging' describes a charging fault).
    prefix = user_words[max(0, start - 3):start]
    if any(word in NEGATION_WORDS for word in prefix):
        return True

    # Also handle 'overheating is not happening' and similar constructions.
    suffix = user_words[end + 1:min(len(user_words), end + 4)]
    if "not" in suffix or "never" in suffix:
        return True

    # If the matched keyword itself contains a polarity word, preserve it.
    if keyword_words.intersection({"not", "no", "without"}):
        return False

    return False


def phrase_matches(user_words, keyword):
    """Return True only for an ordered, non-negated keyword phrase."""
    positions = _phrase_positions(user_words, keyword)
    if positions is None:
        return False
    return not _is_negated(user_words, positions, keyword)


def extract_facts(problem, assertions):
    """Return sorted explicitly supported fact names from assertion keywords."""
    if not isinstance(problem, str) or not problem.strip():
        return []

    user_words = normalize_tokens(problem)
    matched = set()

    for assertion in assertions:
        if not isinstance(assertion, dict):
            continue
        fact_name = assertion.get("fact")
        if not isinstance(fact_name, str) or not fact_name.strip():
            continue

        keywords = list(assertion.get("keywords") or [])
        keywords.append(fact_name.replace("_", " "))
        keywords.extend(FACT_ALIASES.get(fact_name, []))

        for keyword in keywords:
            if not isinstance(keyword, str) or not keyword.strip():
                continue
            positions = _phrase_positions(user_words, keyword)
            if positions is not None and not _is_negated(
                user_words, positions, keyword
            ):
                matched.add(fact_name)
                break

    return sorted(matched)



def extract_negated_facts(problem, assertions):
    """Return facts explicitly mentioned with negative polarity."""
    if not isinstance(problem, str) or not problem.strip():
        return []

    user_words = normalize_tokens(problem)
    negated = set()
    positive = set()

    for assertion in assertions:
        if not isinstance(assertion, dict):
            continue
        fact_name = assertion.get("fact")
        if not isinstance(fact_name, str) or not fact_name.strip():
            continue

        keywords = list(assertion.get("keywords") or [])
        keywords.append(fact_name.replace("_", " "))
        keywords.extend(FACT_ALIASES.get(fact_name, []))

        for keyword in keywords:
            if not isinstance(keyword, str) or not keyword.strip():
                continue
            positions = _phrase_positions(user_words, keyword)
            if positions is None:
                continue
            if _is_negated(user_words, positions, keyword):
                negated.add(fact_name)
            else:
                positive.add(fact_name)
                break

    return sorted(negated - positive)

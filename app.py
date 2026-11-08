
import streamlit as st

st.set_page_config(
    page_title="MobileCare AI",
    page_icon="📱",
    layout="wide"
)

st.title("📱 MobileCare AI")
st.subheader("Android Mobile Troubleshooting Expert System")

st.write(
    "Welcome to MobileCare AI. "
    "Your intelligent assistant for Android mobile problems."
)

st.divider()

st.header("How can we help you?")

problem = st.text_area(
    "Describe your mobile problem:",
    placeholder="Example: My phone battery drains very fast..."
)

if st.button("Diagnose Problem"):
    if problem.strip():
        st.info("Your problem has been received.")
        st.write("Expert System diagnosis will be integrated here.")
    else:
        st.warning("Please describe your mobile problem.")

st.divider()

st.caption("MobileCare AI | BS Artificial Intelligence Major Project")

import streamlit as st
from textblob import TextBlob

st.title("Grammar and Spelling Checker (TextBlob)")

# Use session state to keep corrected text persistent
if 'corrected_text' not in st.session_state:
    st.session_state.corrected_text = ""

# Input area
st.markdown("### Enter your text:")
input_text = st.text_area("", height=200, value=st.session_state.get('input_text', ''))

# When button pressed, run TextBlob correction
if st.button("Correct Grammar"):
    if input_text.strip() == "":
        st.warning("Please enter some text to correct.")
    else:
        blob = TextBlob(input_text)
        corrected = blob.correct()
        st.session_state.corrected_text = str(corrected)
        st.session_state.input_text = input_text
        st.success("✅ Grammar and spelling corrected.")

# Output area (editable)
if st.session_state.corrected_text:
    st.markdown("### Corrected Text:")
    st.session_state.corrected_text = st.text_area("", height=200, value=st.session_state.corrected_text)

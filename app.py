import streamlit as st
from textblob import TextBlob

st.title("Grammar and Spelling Checker (TextBlob)")

# Use session state to keep texts persistent
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "corrected_text" not in st.session_state:
    st.session_state.corrected_text = ""

# Input text area
st.markdown("### Enter your text:")
input_text = st.text_area("", height=200, value=st.session_state.input_text)

# Button to trigger correction
if st.button("Correct Grammar"):
    if not input_text.strip():
        st.warning("Please enter some text to correct.")
    else:
        blob = TextBlob(input_text)
        corrected = blob.correct()
        st.session_state.corrected_text = str(corrected)
        st.session_state.input_text = input_text
        st.success("✅ Grammar and spelling corrected.")

# Output text area (editable)
if st.session_state.corrected_text:
    st.markdown("### Corrected Text:")
    corrected_text = st.text_area("", height=200, value=st.session_state.corrected_text)
    # Update corrected_text in session state if user edits output
    st.session_state.corrected_text = corrected_text

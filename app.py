import streamlit as st
from textblob import TextBlob

st.title("Grammar and Spelling Checker (TextBlob)")

st.markdown("### Enter your text:")
input_text = st.text_area("", height=200)

corrected_text = ""

if st.button("Correct Grammar"):
    if input_text.strip() == "":
        st.warning("Please enter some text to correct.")
    else:
        blob = TextBlob(input_text)
        corrected_text = blob.correct()
        st.success("✅ Grammar and spelling corrected.")

if corrected_text:
    st.markdown("### Corrected Text:")
    corrected_text = st.text_area("", value=str(corrected_text), height=200)

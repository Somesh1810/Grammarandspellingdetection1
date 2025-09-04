import streamlit as st
import requests

st.title("Context-Aware Grammar and Spelling Checker (LanguageTool API)")

input_text = st.text_area("Enter your text:", height=200)

def correct_text_with_languagetool(text):
    url = "https://api.languagetool.org/v2/check"
    data = {
        'text': text,
        'language': 'en-US',
    }
    response = requests.post(url, data=data)
    result = response.json()

    corrected_text = text
    matches = result.get('matches', [])

    # Apply corrections from last to first to keep offsets valid
    for match in reversed(matches):
        offset = match['offset']
        length = match['length']
        replacements = match.get('replacements', [])
        if replacements:
            replacement = replacements[0]['value']
            corrected_text = corrected_text[:offset] + replacement + corrected_text[offset + length:]

    return corrected_text

if st.button("Correct Grammar"):
    if not input_text.strip():
        st.warning("Please enter some text to correct.")
    else:
        corrected = correct_text_with_languagetool(input_text)
        st.success("✅ Grammar and spelling corrected.")
        st.text_area("Corrected Text:", value=corrected, height=200)

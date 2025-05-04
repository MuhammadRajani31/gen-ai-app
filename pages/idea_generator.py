from google import genai
from google.genai import types
import json
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


st.markdown("<h1 style='color: green;'>Startup Idea Generator ✔</h1>", unsafe_allow_html=True)

user_input = st.text_area("What Business problem are you trying to solve? 💡", placeholder="E.g., cookies Business, Education with AI, etc...")



prompt = f"""
Generate a startup plan for the following theme: {user_input}.
Outline the business model, target audience, monetization strategy, and key challenges in short and esure that 
output tokens is 500.
"""

if st.button("Generate Idea"):
    with st.spinner(text="Generating Idea..."):
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content_stream(
            model="gemini-2.0-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=500,
                temperature=0.1
            )
        )
    
        for chunk in response:
            st.write(chunk.text, end="")
    # st.write(response.text)

st.write("---")

st.write("**App created By Muslim**")
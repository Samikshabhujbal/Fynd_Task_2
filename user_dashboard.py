import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from utils import save_entry

# Load .env file
load_dotenv()

# Configure Gemini using hidden API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("⭐ User Review Dashboard")

rating = st.slider("Select Rating", 1, 5)
review = st.text_area("Write your review")

def generate_summary(text):
    model = genai.GenerativeModel("models/gemini-flash-lite-latest")
    prompt = f"Summarize this review and give a short recommendation:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

if st.button("Generate Summary"):
    if review.strip() == "":
        st.error("Please enter a review first.")
    else:
        summary = generate_summary(review)
        st.subheader("AI Summary:")
        st.write(summary)

        save_entry(rating, review, summary)
        st.success("Saved successfully!")

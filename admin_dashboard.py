import streamlit as st
import pandas as pd
from utils import load_entries

st.set_page_config(page_title="Admin Dashboard", page_icon="🛠", layout="wide")

st.title("🛠 Admin Dashboard")
st.write("View all user reviews, ratings, and AI-generated summaries.")

# Load stored data
df = load_entries()

if df.empty:
    st.warning("No submissions found yet!")
else:
    st.subheader("📋 All User Submissions")
    st.dataframe(df, use_container_width=True)

    # Metrics Section
    st.subheader("📊 Summary Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Reviews", len(df))

    with col2:
        most_common_rating = df["user_rating"].mode()[0]
        st.metric("Most Common Rating", most_common_rating)

    with col3:
        avg_rating = round(df["user_rating"].mean(), 2)
        st.metric("Average Rating", avg_rating)

    st.subheader("⭐ Rating Distribution")
    rating_counts = df["user_rating"].value_counts().sort_index()
    st.bar_chart(rating_counts)

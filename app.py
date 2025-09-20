import streamlit as st
from utils import read_file, keyword_match_score, embedding_similarity, highlight_sentences
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Resume Relevance AI", page_icon="🚀", layout="wide")

# Background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("assets/background.jpg");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Resume Relevance AI 🚀")
st.write("Upload Job Description and Resumes to check relevance.")

# Upload files
job_file = st.file_uploader("Upload Job Description (.txt or .pdf)", type=["txt","pdf"])
resume_files = st.file_uploader("Upload Resume(s) (.txt or .pdf)", type=["txt","pdf"], accept_multiple_files=True)

if job_file and resume_files:
    job_text = read_file(job_file)
    results = []

    for file in resume_files:
        resume_text = read_file(file)

        # Calculate scores
        keyword_score, matched_keywords = keyword_match_score(job_text, resume_text)
        embedding_score = embedding_similarity(job_text, resume_text)
        matched_sentences = highlight_sentences(job_text, resume_text)

        # Determine relevance category
        if embedding_score > 70:
            category = "High"
            color = "green"
        elif embedding_score > 40:
            category = "Medium"
            color = "orange"
        else:
            category = "Low"
            color = "red"

        results.append({
            "Resume": file.name,
            "Keyword Score (%)": keyword_score,
            "Embedding Score (%)": embedding_score,
            "Category": category,
            "Color": color,
            "Matched Keywords": ", ".join(list(matched_keywords)),
            "Matched Sentences": " | ".join(matched_sentences[:5])
        })

    # Convert results to DataFrame
    df = pd.DataFrame(results)
    st.subheader("Resume Relevance Results")

    # Display scores as metrics in columns
    for index, row in df.iterrows():
        col1, col2, col3 = st.columns(3)
        col1.metric("Resume", row["Resume"])
        col2.metric("Embedding Score (%)", row["Embedding Score (%)"], delta=None)
        col3.markdown(f"<span style='color:{row['Color']};font-weight:bold'>{row['Category']} Relevance</span>", unsafe_allow_html=True)

    # Display detailed table
    st.subheader("Detailed Table")
    st.dataframe(df[["Resume","Keyword Score (%)","Embedding Score (%)","Category","Matched Keywords","Matched Sentences"]])

    # Plot bar chart
    fig, ax = plt.subplots(figsize=(8,5))
    df.plot(x="Resume", y=["Keyword Score (%)","Embedding Score (%)"], kind="bar", ax=ax, color=["skyblue","limegreen"])
    plt.title("Resume Relevance Scores")
    plt.ylabel("Score (%)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Downloadable CSV report
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Report as CSV",
        data=csv,
        file_name="resume_relevance_report.csv",
        mime="text/csv"
    )
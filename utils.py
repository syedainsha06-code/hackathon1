import PyPDF2
from sentence_transformers import SentenceTransformer, util

# Load embedding model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def read_file(file):
    """Read PDF or TXT file"""
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    else:
        return str(file.read(), "utf-8")

def keyword_match_score(job_text, resume_text):
    """Basic keyword match"""
    job_words = set(job_text.lower().split())
    resume_words = set(resume_text.lower().split())
    matched_keywords = job_words & resume_words
    score = round((len(matched_keywords) / len(job_words)) * 100, 2)
    return score, matched_keywords

def embedding_similarity(job_text, resume_text):
    """Compute semantic similarity using embeddings"""
    job_embedding = model.encode(job_text, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    similarity = util.cos_sim(job_embedding, resume_embedding).item() * 100
    return round(similarity, 2)

def highlight_sentences(job_text, resume_text):
    """Return sentences from resume that match job description context"""
    resume_sentences = resume_text.split('.')
    matched_sentences = [s for s in resume_sentences if any(word in job_text for word in s.split())]
    return matched_sentences
# hackathon1
Automated Resume Relevence Check Sysytem

This explains the idea, setup, usage, and enhancements clearly.

📄 Resume Relevance AI

An AI-powered Resume Relevance Checker built with Streamlit and Sentence Transformers.
The app compares a resume against a job description and provides:

✅ Relevance Score (Keywords + Semantic Similarity)
✅ Keyword Matches (highlighted words/phrases)
✅ Skill Coverage (based on predefined skill sets)
✅ Resume Insights (contextual matching sentences)
✅ Polished UI with background image and metrics

---
🚀 Features

Upload Resume (PDF/TXT) & Job Description (PDF/TXT)

Automatic keyword extraction and semantic similarity scoring

Skill matching dashboard with percentage scores

Beautiful Streamlit UI with custom background image

Optimized for low-memory systems with lightweight models

---
📂 Project Structure

resume-relevance-hackathon-polished/
│
├─ app.py                 # Main Streamlit app
├─ utils.py               # Functions for scoring & analysis
├─ requirements.txt       # Python dependencies
├─ README.md              # Project documentation
│
├─ assets/
│   └─ background.jpg     # Background image for UI
│
└─ data/                  # (Optional) Sample resumes & job descriptions

---

⚙ Installation

1️⃣ Clone the repository

git clone https://github.com/your-username/resume-relevance-ai.git
cd resume-relevance-ai

2️⃣ Create a virtual environment

python -m venv venv

Activate it:

Windows (PowerShell):

.\venv\Scripts\activate


3️⃣ Install dependencies

pip install -r requirements.txt

---

▶ Usage

1. Place your background image in the assets/ folder as background.jpg.


2. Run the app:

streamlit run app.py


3. Upload:

Resume (PDF/TXT)

Job Description (PDF/TXT)



4. View results:

Keyword Match Score

Semantic Similarity Score

Skill Match Percentages

Overall Relevance

---

📊 Example Output

Relevance Score: 78% (High)

Matched Keywords: ['python', 'machine learning', 'sql']

Skill Coverage: Python ✅, SQL ✅, TensorFlow ❌

Resume Insights: Highlighted matching sentences

---

🔧 Enhancements (Future Work)

Multi-resume bulk matching for recruiters

Dashboard with shortlisting recommendations

Export results to CSV / Excel

Integrate with LinkedIn API for auto job scraping

Support for DOCX resumes

👉 Do you also want me to give you a sample requirements.txt that matches your optimized utils.py (with lightweight transformer model)?

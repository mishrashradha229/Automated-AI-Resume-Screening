import streamlit as st

from candidate import Candidate
from parser import ResumeParser
from skill_extractor import SkillExtractor
from ats_score import ATSScore
from db import Database
from heap_ranking import HeapRanking

st.title(
"Ai Powered Resume Screener"
)

jd = st.text_area(
"Enter Job Description"
)

files = st.file_uploader(
"upload Resumes",
type=["pdf"],
accept_multiple_files= True
)

if st.button("Analyze"):
  parser = ResumeParser()
  extractor = SkillExtractor()
  scorer = ATSScore()

  db = Database()
  candidates = []

  for file in files:
    text = parser.extract_text(file)

    skills = extractor.extract_skills(text)

    score = scorer.calculate_score(
      jd,
      text
    )

    candidate = Candidate(
      file.name,
      file.name,
      skills
    )
    candidate.set_score(score)
    candidates.append(candidate)
    candidate_id = db.save_candidate(
      candidate
    )

  top_candidates = HeapRanking.top_candidates(
    candidates,
    10
  )

  st.subheader(
    "Top Ranker Candidates"
  )

  rank = 1

  for candidate in top_candidates:
    st.write(
    f"""
    Rank = {rank}
    Name = {candidate.name}
    Score = {candidate.score} %
    Skills = {candidate.skills}
    """
    )

    rank += 1
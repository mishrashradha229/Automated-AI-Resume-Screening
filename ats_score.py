from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ATSScore:
  def calculate_score(
    self,
    jd,
    resume_text
  ):

    docs = [jd,resume_text]
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(docs)
    similarity = cosine_similarity(
      matrix[0:1],
      matrix[1:2]
    )

    return round(
      similarity[0][0] * 100,
      2
    )

  

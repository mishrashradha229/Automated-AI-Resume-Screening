import pandas as pd

class SkillExtractor:

  def __init__(self):

    self.skills = pd.read_csv(
      "data/skills.csv"
    )["Skill"].tolist()

  def extract_skills(
      self,
      text
  ):
    
    found = []
    for skill in self.skills:
      if skill in self.skills:
        found.append(skill)
    return found

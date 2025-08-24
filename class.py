class Movie:
  def __init__(self,title,year,score):
    self.title = title
    self.year = year
    self.score = score

  def nprint(self):
    print(f"Title : ",self.title)
    print(f"year : ",self.year)
    print(f"score : ",self.score)

hero = Movie("Hero", 2005, 9.3)
Mars = Movie("Mars", 2005, 9.3)
Movie.nprint(hero)
Movie.nprint(Mars)
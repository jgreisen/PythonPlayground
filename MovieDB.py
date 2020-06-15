# Adding a comment

class Movie:
  def __init__(self, title, rating):
    self.title = title
    self.rating = rating

movieDB = []

def addMovie(Movie):
  movieDB.append(Movie)

def printMovies(list):
  for x, movie in enumerate(list):
    print('The movie at index {} in our movie database is named {} and has an {} rating.'.format(str(x), movie.title, movie.rating))


print('Adding John Wick to our movie database via append...')
movieDB.append(Movie("John Wick", "R"))
printMovies(movieDB)

print('Adding Jaws to our movie database via function...')
addMovie(Movie("Jaws", "R"))
printMovies(movieDB)

print('Add a new movie to our database!')
print('Please enter a movie title:')
movieName = input()
print('Please enter a movie rating:')
movieRating = input()

movieDB.append(Movie(movieName, movieRating))
printMovies(movieDB)

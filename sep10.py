
import pandas

movies = 'data/movielens/movies.csv'
users = 'data/movielens/users.csv'
ratings = 'data/movielens/ratings.csv'


m = pandas.read_csv(movies)

print(m.genres.unique)
print(m.genres.value_counts().head(10))
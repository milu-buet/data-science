# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataScience - Assignment 2 

import pandas as pd

movies = pd.read_csv('movielens/movies.csv')
ratings = pd.read_csv('movielens/ratings.csv')
users = pd.read_csv('movielens/users.csv')

ratings_users = pd.merge(ratings,users,on='user_id')
ratings_movies = pd.merge(ratings,movies,on='movie_id')
ratings_users_movies  = pd.merge(ratings_users,movies,on='movie_id')


def get_highly_rated_movies_by_females():
		
	df = ratings_users_movies[ratings_users_movies.gender == 'F']
	df = df[['user_id','movie_id','title','rating']]
	df = df.groupby('title')[['rating']].mean()
	df = df.sort_values('rating', ascending = False)

	return df.head(10)


def get_highly_rated_movies_by_males():
		
	df = ratings_users_movies[ratings_users_movies.gender == 'M']
	df = df[['user_id','movie_id','title','rating']]
	df = df.groupby('title')[['rating']].mean()
	df = df.sort_values('rating', ascending = False)

	return df.head(10)


def get_most_rated_movies_for_group_18():
 	#pass
	df = ratings_users_movies[ratings_users_movies.age == 18]
	df = df[['user_id','movie_id','title','rating']]
	df = df.groupby('title')['rating'].count().to_frame()
	df = df.sort_values('rating', ascending = False)

	return df.head(10)


def get_highest_average_rating_movies_for_group_18():
 	#pass
	df = ratings_users_movies[ratings_users_movies.age == 18]
	df = df[['user_id','movie_id','title','rating']]
	df = df.groupby('title')['rating'].mean().to_frame()
	df = df.sort_values('rating', ascending = False)

	return df.head(10)



def get_most_higly_rated_action_movies():
 	#pass
	df = ratings_users_movies[ratings_users_movies.genres == 'Action|Crime|Thriller']
	df = df[['user_id','movie_id','title','rating']]
	df = df.groupby('title')['rating'].mean().to_frame()
	df = df.sort_values('rating', ascending = False)

	return df.head(10)


def get_most_higly_rated_comedy_movies():
 	#pass
	df = ratings_users_movies[ratings_users_movies.genres == 'Comedy|Romance|Thriller']
	df = df[['user_id','movie_id','title','rating']]
	df = df.groupby('title')['rating'].mean().to_frame()
	df = df.sort_values('rating', ascending = False)

	return df.head(20)


def get_pivot():
	df = ratings_users_movies[ ratings_users_movies.age == 18]
	df = pd.pivot_table(ratings_users_movies, index = 'title', columns='gender', values='rating', fill_value='N/A')

	return df


def get_df_f6():
 	#pass
	df = ratings_users_movies#[ratings_users_movies.gender == gender[0]]
	df = df.groupby(['gender','age'])['rating'].mean().to_frame()
	#df = df.sort_values('age')
	#df = df.rename(index=str, columns = { "rating": gender})

	return df.reset_index()

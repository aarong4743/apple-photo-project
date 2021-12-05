import os
if __name__ == "__main__":

	# Grab all movies in the current photos library
	os.chdir("/Users/Aaron/Pictures/Photos Library.photoslibrary")
	os.system("find . -name '*.avi' > /Users/Aaron/Programming/apple-photo-project/current_movie_out.txt")
	os.system("find . -name '*.AVI' >> /Users/Aaron/Programming/apple-photo-project/current_movie_out.txt")
	os.system("find . -name '*.mov' >> /Users/Aaron/Programming/apple-photo-project/current_movie_out.txt")
	os.system("find . -name '*.MOV' >> /Users/Aaron/Programming/apple-photo-project/current_movie_out.txt")
	os.system("find . -name '*.mpg' >> /Users/Aaron/Programming/apple-photo-project/current_movie_out.txt")
	os.chdir("/Users/Aaron/Programming/apple-photo-project")
	with open("current_movie_out.txt", "r") as f:
		current_movies = f.readlines()
	print(str(len(current_movies)) + " total current movies")
	movie_names = []
	movie_times = []
	for i in range(len(current_movies)):
		movie = current_movies[i][current_movies[i].rfind("/", 0, current_movies[i].rfind("/"))+1:len(current_movies[i])-1]
		movie_names.append(movie[movie.find("/")+1:])
		movie_times.append(movie[0:movie.find("/")])

	movie_set = []
	duplicate_movie_names = []
	duplicate_movie_times = []
	for i in range(len(movie_names)):

		# New movies go into the movie set
		if movie_names[i] not in movie_set:
			movie_set.append(movie_names[i])

		# Movies that have already been found are duplicates. Add them to a different list.
		else:
			duplicate_movie_names.append(movie_names[i])
			duplicate_movie_times.append(movie_times[i])

	# Print out all duplicate movies
	print(str(len(duplicate_movie_names)) + " duplicate movies have been found:\n")
	for i in range(len(duplicate_movie_names)):
		print(duplicate_movie_names[i] + " at " + duplicate_movie_times[i])

	os.system("rm current_movie_out.txt")
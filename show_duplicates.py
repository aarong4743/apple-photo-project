import os
import sys
import time
if __name__ == "__main__":

	# Grab all movies in the current photos library
	PHOTO_LIB = "/Users/Aaron/Pictures/Photos\ Library.photoslibrary"
	os.system("find {} -name '*.avi' > current_movie_out.txt".format(PHOTO_LIB))
	os.system("find {} -name '*.AVI' >> current_movie_out.txt".format(PHOTO_LIB))
	os.system("find {} -name '*.mov' >> current_movie_out.txt".format(PHOTO_LIB))
	os.system("find {} -name '*.MOV' >> current_movie_out.txt".format(PHOTO_LIB))
	os.system("find {} -name '*.mpg' >> current_movie_out.txt".format(PHOTO_LIB))
	with open("current_movie_out.txt", "r") as f:
		current_movies = f.readlines()
	print(str(len(current_movies)) + " total movie(s) in the photo library\n")

	# Iterate through all movies and get the name, time, and size of each movie
	movie_names = []
	movie_times = []
	movie_sizes = []
	for i in range(len(current_movies)):
		movie = current_movies[i][:len(current_movies[i])-1]
		movie_cut = movie[movie.rfind("/", 0, movie.rfind("/"))+1:len(movie)]
		movie_names.append(movie_cut[movie_cut.find("/")+1:])
		movie_times.append(movie_cut[0:movie_cut.find("/")])
		movie_sizes.append(os.path.getsize(movie))

	# First, we want to check flag videos as duplicates if they are the same size. 
	# Then, we want to flag videos as duplicates if they are the same name.
	filter_variants = ['size', 'name']
	for filter_variant in filter_variants:
		movie_names_set = []
		movie_times_set = []
		movie_sizes_set = []
		duplicate_movie_names = []
		duplicate_movie_times = []
		original_movie_names = []
		original_movie_times = []
		if filter_variant == 'size':
			list_to_check = movie_sizes
			set_to_check = movie_sizes_set
		elif filter_variant == 'name':
			list_to_check = movie_names
			set_to_check = movie_names_set

		# Iterate through all of the movies again
		for i in range(len(movie_sizes)):
			# New movies go into the movie set
			if list_to_check[i] not in set_to_check:
				movie_names_set.append(movie_names[i])
				movie_times_set.append(movie_times[i])
				movie_sizes_set.append(movie_sizes[i])

			# Movies that have already been found are duplicates.
			else:
				# Get the index of the original movie in the set 
				original_index = set_to_check.index(list_to_check[i])
				# If we are filtering movies based on name,
				# then if the two movies with the matching name have the same size,
				# then ignore as we have already previously filtered by size 
				if filter_variant == "name":
					if movie_sizes[i] == movie_sizes_set[original_index]:
						continue
				# Add the duplicate movie to the duplicate lists
				duplicate_movie_names.append(movie_names[i])
				duplicate_movie_times.append(movie_times[i])
				# Add the original movie to the original list
				original_movie_names.append(movie_names_set[original_index])
				original_movie_times.append(movie_times_set[original_index])

		# Print out all duplicate movies and show their original counterparts
		if filter_variant == 'size':
			print(str(len(duplicate_movie_names)) + " duplicate movie(s) based on filtering by movie size.\n")
		else:
			print(str(len(duplicate_movie_names)) + " duplicate movie(s) based on filtering by movie name, excluding movies that match by size.\n")

		print("Format:\n\n(duplicate movie name) from (duplicate movie time) -> (original movie name) from (original movie time)\n")

		for i in range(len(duplicate_movie_names)):
			print(duplicate_movie_names[i] + " from " + duplicate_movie_times[i] + " -> " + original_movie_names[i] + " from " + original_movie_times[i])
		if filter_variant == "size":
			print("\n\n\n")

	os.system("rm current_movie_out.txt")
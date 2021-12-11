import os
if __name__ == "__main__":

	# Grab all movies in the backup photos library
	BACKUP_PHOTO_LIB = "/Extra\ Backups/iMac\ System\ Photos\ Library\ Backup/Photos\ Library.photoslibrary"
	os.system("find {} -name '*.avi' > backup_movie_out.txt".format(BACKUP_PHOTO_LIB))
	os.system("find {} -name '*.AVI' >> backup_movie_out.txt".format(BACKUP_PHOTO_LIB))
	os.system("find {} -name '*.mov' >> backup_movie_out.txt".format(BACKUP_PHOTO_LIB))
	os.system("find {} -name '*.MOV' >> backup_movie_out.txt".format(BACKUP_PHOTO_LIB))
	os.system("find {} -name '*.mpg' >> backup_movie_out.txt".format(BACKUP_PHOTO_LIB))
	with open("backup_movie_out.txt", "r") as f:
		backup_movies = f.readlines()
	print(str(len(backup_movies)) + " total movie(s) in the backup photo library\n")

	# Iterate through all movies in the backup photo library and get the name, time, and size of each movie
	backup_movie_names = []
	backup_movie_times = []
	backup_movie_sizes = []
	for i in range(len(backup_movies)):
		movie = backup_movies[i][:len(backup_movies[i])-1]
		movie_cut = movie[movie.rfind("/", 0, movie.rfind("/"))+1:len(movie)]
		backup_movie_names.append(movie_cut[movie_cut.find("/")+1:])
		backup_movie_times.append(movie_cut[0:movie_cut.find("/")])
		backup_movie_sizes.append(os.path.getsize(movie))

	# Grab all movies in the current photos library
	PHOTO_LIB = "/Users/Aaron/Pictures/Photos\ Library.photoslibrary"
	os.system("find {} -name '*.avi' > current_movie_out.txt".format(PHOTO_LIB))
	os.system("find {} -name '*.AVI' >> current_movie_out.txt".format(PHOTO_LIB))
	os.system("find {} -name '*.mov' >> current_movie_out.txt".format(PHOTO_LIB))
	os.system("find {} -name '*.MOV' >> current_movie_out.txt".format(PHOTO_LIB))
	os.system("find {} -name '*.mpg' >> current_movie_out.txt".format(PHOTO_LIB))
	with open("current_movie_out.txt", "r") as f:
		current_movies = f.readlines()
	print(str(len(current_movies)) + " total movie(s) in the current photo library\n")

	# Iterate through all movies in the current photo library and get the name, time, and size of each movie
	current_movie_names = []
	current_movie_times = []
	current_movie_sizes = []
	for i in range(len(current_movies)):
		movie = current_movies[i][:len(current_movies[i])-1]
		movie_cut = movie[movie.rfind("/", 0, movie.rfind("/"))+1:len(movie)]
		current_movie_names.append(movie_cut[movie_cut.find("/")+1:])
		current_movie_times.append(movie_cut[0:movie_cut.find("/")])
		current_movie_sizes.append(os.path.getsize(movie))

	# First, we want to search for missing movies based on missing movie sizes
	# Then, we want to search for missing movies based on missing movie names
	filter_variants = ['size', 'name']
	for filter_variant in filter_variants:
		if filter_variant == 'size':
			backup_list = backup_movie_sizes
			current_list = current_movie_sizes
		elif filter_variant == 'name':
			backup_list = backup_movie_names
			current_list = current_movie_names
		# If a movie is in the backup photos library and NOT in the current photos library, that means we have accidentally deleted a non-duplicate. Add it to the list.
		bad_movie_names = []
		bad_movie_times = []
		for i in range(len(backup_movie_names)):
			if backup_list[i] not in current_list:
				bad_movie_names.append(backup_movie_names[i])
				bad_movie_times.append(backup_movie_times[i])

		# Print out all non-duplicates accidentally deleted, showing movie name and movie time
		if filter_variant == 'size':
			print(str(len(bad_movie_names)) + " non-duplicate movie(s) accidentally deleted based on filtering by movie size:\n")
		else:
			print(str(len(bad_movie_names)) + " non-duplicate movie(s) accidentally deleted based on filtering by movie name, excluding movies that match by size:\n")
		print("Format:\n(movie name) from (movie time)\n")
		for i in range(len(bad_movie_names)):
			print(bad_movie_names[i] + " from " + bad_movie_times[i])
		if filter_variant == 'size':
			print("\n\n\n")

	os.system("rm backup_movie_out.txt")
	os.system("rm current_movie_out.txt")
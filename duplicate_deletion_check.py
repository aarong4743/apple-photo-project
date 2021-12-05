import os
if __name__ == "__main__":

	# Grab all movies in the backup photos library 
	os.chdir("/Extra Backups/iMac System Photos Library Backup/Photos Library.photoslibrary")
	os.system("find . -name '*.avi' > /Users/Aaron/Programming/Photo_Project/backup_movie_out.txt")
	os.system("find . -name '*.AVI' >> /Users/Aaron/Programming/Photo_Project/backup_movie_out.txt")
	os.system("find . -name '*.mov' >> /Users/Aaron/Programming/Photo_Project/backup_movie_out.txt")
	os.system("find . -name '*.MOV' >> /Users/Aaron/Programming/Photo_Project/backup_movie_out.txt")
	os.system("find . -name '*.mpg' >> /Users/Aaron/Programming/Photo_Project/backup_movie_out.txt")
	os.chdir("/Users/Aaron/Programming/Photo_Project")
	with open("backup_movie_out.txt", "r") as f:
		backup_movies = f.readlines()
	print(str(len(backup_movies)) + " total backup movies")
	backup_movie_names = []
	backup_movie_times = []
	for i in range(len(backup_movies)):
		movie = backup_movies[i][backup_movies[i].rfind("/", 0, backup_movies[i].rfind("/"))+1:len(backup_movies[i])-1]
		backup_movie_names.append(movie[movie.find("/")+1:])
		backup_movie_times.append(movie[0:movie.find("/")])

	# Grab all movies in the current photos library
	os.chdir("/Users/Aaron/Pictures/Photos Library.photoslibrary")
	os.system("find . -name '*.avi' > /Users/Aaron/Programming/Photo_Project/current_movie_out.txt")
	os.system("find . -name '*.AVI' >> /Users/Aaron/Programming/Photo_Project/current_movie_out.txt")
	os.system("find . -name '*.mov' >> /Users/Aaron/Programming/Photo_Project/current_movie_out.txt")
	os.system("find . -name '*.MOV' >> /Users/Aaron/Programming/Photo_Project/current_movie_out.txt")
	os.system("find . -name '*.mpg' >> /Users/Aaron/Programming/Photo_Project/current_movie_out.txt")
	os.chdir("/Users/Aaron/Programming/Photo_Project")
	with open("current_movie_out.txt", "r") as f:
		current_movies = f.readlines()
	print(str(len(current_movies)) + " total current movies")
	current_movie_names = []
	current_movie_times = []
	for i in range(len(current_movies)):
		movie = current_movies[i][current_movies[i].rfind("/", 0, current_movies[i].rfind("/"))+1:len(current_movies[i])-1]
		current_movie_names.append(movie[movie.find("/")+1:])

	# If a movie is in the backup photos library and NOT in the current photos library, that means we have accidentally deleted a non-duplicate. Add it to the list.
	bad_movie_names = []
	bad_movie_times = []
	for i in range(len(backup_movie_names)):
		if backup_movie_names[i] not in current_movie_names:
			bad_movie_names.append(backup_movie_names[i])
			bad_movie_times.append(backup_movie_times[i])

	# Print out all non-duplicates accidentally deleted
	print(str(len(bad_movie_names)) + " non-duplicate(s) accidentally deleted:\n")
	for i in range(len(bad_movie_names)):
		print(bad_movie_names[i] + " at " + bad_movie_times[i])
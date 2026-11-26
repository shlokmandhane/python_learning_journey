#WAP to as the user to enter names of their three favourite movies and store them in a list.

Movies = []

movie_1 = input("Enter the name of the first movie: ")
movie_2 = input("Enter the name of the second movie: ")
movie_3 = input("Enter the name of the third movie: ")

Movies.append(movie_1)
Movies.append(movie_2)
Movies.append(movie_3)

print("Your top 3 favourite movies are:", Movies)
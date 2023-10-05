movie_database = {}

while True:
    print("\nMenu:")
    print("1. Add a movie")
    print("2. Update a movie")
    print("3. Delete a movie")
    print("4. View all movies")
    print("5. Exit")

    choice = input("Please choose an option (1-5): ")

    if choice == "1":
        title = input("Enter movie title: ")
        director = input("Enter director: ")
        release_year = input("Enter release year: ")
        genre = input("Enter genre: ")

        movie_database[title] = {
            "Director": director,
            "Release Year": release_year,
            "Genre": genre,
        }
        print(f"{title} has been added to the database.")

    elif choice == "2":
        title = input("Enter the title of the movie to update: ")
        if title in movie_database:
            director = input("Enter new director: ")
            release_year = input("Enter new release year: ")
            genre = input("Enter new genre: ")

            movie_database[title] = {
                "Director": director,
                "Release Year": release_year,
                "Genre": genre,
            }
            print(f"{title} has been updated.")
        else:
            print(f"{title} not found in the database.")

    elif choice == "3":
        title = input("Enter the title of the movie to delete: ")
        if title in movie_database:
            del movie_database[title]
            print(f"{title} has been deleted.")
        else:
            print(f"{title} not found in the database.")

    elif choice == "4":
        if not movie_database:
            print("The movie database is empty.")
        else:
            print("\nMovie Database:")
            for title, info in movie_database.items():
                print(f"Title: {title}")
                print(f"Director: {info['Director']}")
                print(f"Release Year: {info['Release Year']}")
                print(f"Genre: {info['Genre']}")
                print()

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please choose a valid option (1-5).")

print("Goodbye!")

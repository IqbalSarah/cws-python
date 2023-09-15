playlist = []

while True:
    print("\nMenu")
    print("1. Add a song to the playlist")
    print("2. Remove a song from the playlist")
    print("3. View the current playlist")
    print("4. Quit")

    choice = input("Please choose an option from the menu : ")

    if choice == "1":
        song = input("Enter the name of the song to add: ")
        playlist.append(song)
        print(f"'{song}' has been added to the playlist.")
    elif choice == "2":
        song = input("Enter the name of the song to remove: ")
        if song in playlist:
            playlist.remove(song)
            print(f"'{song}' has been removed from the playlist.")
        else:
            print(f"'{song}' is not in the playlist.")
    elif choice == "3":
        print("\nCurrent Playlist:")
        if not playlist:
            print("The playlist is empty.")
        else:
            for i in range(len(playlist)):
                print(f"{i+1}. {playlist[i]}")
    elif choice == "4":
        print("Thank you for using the Music Playlist Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option from the menu.")

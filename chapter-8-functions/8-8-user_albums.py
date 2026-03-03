# CloudOfNiko
# 03.03.2026
# Learning to use functions in Python.

def make_album(artist_name, album_title):
    """Create a dictionary with information about a music album."""
    album = {'artist' : artist_name, 'title' : album_title}
    return album
    
while True:
    print("\nPlease enter the album information:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Enter artist: ")
    if artist_name == 'q':
        break
        
    album_title = input("Enter album title: ")
    if album_title == 'q':
        break
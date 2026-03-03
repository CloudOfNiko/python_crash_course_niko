# CloudOfNiko
# 03.03.2026
# Learning to use functions in Python.

def make_album(artist_name, album_title, songs_count=None):
    """Create a dictionary with information about a music album."""
    album = {'artist' : artist_name, 'title' : album_title}
    
    if songs_count:
        album['songs'] = songs_count
    return album

foo = make_album('Foo Fighters', 'Echoes, Silence & Grace')
paige = make_album('Jamie Paige', 'Constant Companions')
now = make_album('Gorillaz', 'The Now Now')

cadet = make_album('Nigel Good', 'Space Cadet', '12')

print(foo)
print(paige)
print(now)
print(cadet)
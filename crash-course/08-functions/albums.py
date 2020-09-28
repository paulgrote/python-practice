# 8-7 

def make_album(album_name,artist_name):
    album = {'title':album_name,'artist':artist_name}

    return album

album = make_album('the sign', 'ace of base')
print(album)

album = make_album('texas flood', 'stevie ray vaughan')
print(album)

album = make_album('made up mind', 'tedeschi trucks band')
print(album)

# 8-8
def make_album(album_name,artist_name):
    album = {'title':album_name,'artist':artist_name}

    return album

while True:
    print("Enter an album.")
    print("Type 'q' at any time to quit.")

    album_name = input("Enter an album name: ")
    if album_name == 'q':
        break

    artist_name = input("Enter the artist name: ")
    if artist_name == 'q':
        break

    album = make_album(album_name, artist_name)
    print(album)
def make_album(artist, title, tracks=0):
    album_dict = {
        'ca si': artist.title(),
        'ten': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

title_prompt = "\nbạn đang nghĩ đến album nào? "
artist_prompt = "ai hát? "

print("ấn 'quit' để stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

def make_album(artist, title):
    album_dict = {
        'ca si': artist.title(),
        'ten': title.title(),
        }
    return album_dict

album = make_album('hieu', 'chay ngay di')
print(album)

album = make_album('chien', 'nhu hom qua')
print(album)

album = make_album('hkt', 'shshsh')
print(album)
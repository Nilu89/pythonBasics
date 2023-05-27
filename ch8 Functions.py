print(8.1)
def display_message(name):
    """Display what I am learning """
    print(f"{name.title()} is learning functions.")
display_message('nilufar')
display_message('nargiza')

print(f"\n8.2 Favorite book")
def favorite_book(title):
    print(f"One of my favorite book is {title}.")
favorite_book('Alice in Wonderland')
favorite_book('An Invisible thread')

print(f'\n8.3 T-shirt')
print('positional')
def make_shirt(size):
    """Display shirt size."""
    print(f"This T-shirt size is {size.upper()}.")
make_shirt('xs')
make_shirt('s')
make_shirt('m')
print(f'\nkeyword')
def make_shirt(size):
    """Display shirt size."""
    print(f"This T-shirt size is {size.upper()}.")
make_shirt(size='xs')
make_shirt(size='s')
make_shirt(size='m')
print(f'\n8.4 Large shirts')
def make_shirt(size='large'):
    """Display shirt size."""
    print(f"I love Python")
make_shirt()
def make_shirt(size='medium'):
    """Display shirt size."""
    print(f"I love Python.")
make_shirt()
def make_shirt(size):
    """Display shirt size."""
    print(f"I love IT. My size is {size.upper()}.")
make_shirt('s')
make_shirt('m')
print(f'\n8.5 Cities')
def describe_city(city, country='US'):
    """The cities which located in the US."""
    print(f"The {city.title()} located in the {country.upper()}.")
describe_city('new york')
describe_city('michigan')
describe_city('paris')

print(f'\n8.6 City names')
def city_country(city_name, country_name):
    return f"{city_name}, {country_name}"
print(city_country('Berlin', 'Germany'))
print(city_country('Tashkent', 'Uzbekistan'))
print(city_country('Dushanbe', 'Tadjikistan'))
print(city_country('Tokiyo', 'Japan'))

print(f'\n8.7 Album(using dictionary)')
def make_album(artist_name, album_title, musics = None):
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if musics:
        album['songs'] = musics
    return album
print(make_album('Ziyoda', 'Yonimda', 'Tor kocha'))
print(make_album('alisher fayz', 'Rashk qilasanmi', 'Onasi'))
print(make_album('yulduz usmonova', 'muhabbat', 'sevgi'))

print(f'\n8.8 User Albums (using while loop)')
def make_album(artist_name, album_title, musics):
    music_album = f"{artist_name.title()} {album_title.title()} {musics.title()}"
    return music_album
while True:
    print("\nPlease, tell artist's name:")
    print("Enter 'q' at any time to quit")

    artist = input("artist_name:")
    if artist == 'q':
        break
    title = input("album_title:")
    if title == 'q':
        break
    musics = input('songs:')
    if musics == 'q':
        break
    album = make_album(artist, title, musics)
    print(f"\nHello, {artist}, is this '{title}' your album?")

print(f'\n8.9 Messages')
def show_messages(names):
    for name in names:
        print(f"Hello, {name.title()}! How are you doing?")
        print(f"What is the weather today?")
users = ['lily', 'john', 'nori']
show_messages(users)


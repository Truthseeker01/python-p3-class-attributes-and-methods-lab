class Song:

    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre:str):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.count = 0
        self.add_song_to_count()
        self.add_to_genres(genre=genre)
        self.add_to_artists(artist=artist)
        self.add_to_genre_count(genre=genre)
        self.add_to_artist_count(artist=artist)
    
    @classmethod
    def add_song_to_count(self):
        self.count += 1
        return self.count
    @classmethod
    def add_to_genres(self, genre):
        self.genres.append(genre)
        return self.genres
    @classmethod
    def add_to_artists(self, artist):
        self.artists.append(artist)
        return self.artists
    @classmethod
    def add_to_genre_count(self, genre):
        self.genre_count[genre] = self.genres.count(genre)
    @classmethod
    def add_to_artist_count(self, artist):
        self.artist_count[artist] = self.artists.count(artist)
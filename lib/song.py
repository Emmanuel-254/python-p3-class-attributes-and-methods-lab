class Song:
    # Class attributes to store overall song data
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes for song details
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the total song count when a new song is created
        Song.add_to_count()
        
        # Add artist and genre to the class attributes
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        
        # Update genre count and artist count
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_to_count(cls):
        """Increments the song count by 1 every time a new song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds the genre to the genres list if it is not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds the artist to the artists list if it is not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Adds a count for the genre in genre_count dictionary."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Adds a count for the artist in artist_count dictionary."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
pass

# Creating songs
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Hotline Bling", "Drake", "Pop")
song3 = Song("Formation", "Beyonce", "Pop")
song4 = Song("Run This Town", "Jay-Z", "Rap")
song5 = Song("God's Plan", "Drake", "Rap")
song6 = Song("Halo", "Beyonce", "Pop")
song7 = Song("Thriller", "Michael Jackson", "Pop")

# Accessing class attributes
print(Song.count)  # Total number of songs
print(Song.artists)  # List of unique artists
print(Song.genres)  # List of unique genres
print(Song.genre_count)  # Count of songs per genre
print(Song.artist_count)  # Count of songs per artist

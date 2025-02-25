"""
DSC 20 Winter 2025 Homework 07
Name: Jaden Goelkel
PID: A18247795
Source: Lecture slides
"""

# Question 1
def type_with_number(message):
    """
    Takes a string and returns a string of numbers based on the type of \
    each character
    
    >>> type_with_number('Welcome to Beijing!')
    '9352663086023454641'
    >>> type_with_number('I miss my laptop.')
    '40647706905278671'
    >>> type_with_number('!!??..  ,,')
    '1111110011'

    # Add at least 3 doctests below here #
    
    """
    if len(message) == 0:
        return ''
    result = None
    if message[0] in ',.?!':
        result = 1
    elif message[0].lower() in 'abc':
        result = 2
    elif message[0].lower() in 'def':
        result = 3
    elif message[0].lower() in 'ghi':
        result = 4
    elif message[0].lower() in 'jkl':
        result = 5
    elif message[0].lower() in 'mno':
        result = 6
    elif message[0].lower() in 'pqrs':
        result = 7
    elif message[0].lower() in 'tuv':
        result = 8
    elif message[0].lower() in 'wxyz':
        result = 9
    elif message[0] == ' ':
        result = 0
        
    return str(result) + type_with_number(message[1:])
        

# Question 2
def make_palindrome(start, stop):
    """
    makes a palindrome string from start to stop numbers

    >>> make_palindrome(1, 1)
    '1'
    >>> make_palindrome(3, 5)
    '34543'
    >>> make_palindrome(5, 2)
    '5432345'

    # Add at least 3 doctests below here #
    """
    if start == stop: 
        return  str(stop)
    if start < stop:
        return str(start) + make_palindrome(start + 1, stop) + str(start)
    if start > stop:    
        return str(start) + make_palindrome(start - 1, stop) + str(start)

# Question 3
def doctests_q3():
    """
    >>> my_phone = Phone('Apple', 4000, 64000)
    >>> my_phone.brand
    'Apple'
    >>> my_phone.charge
    2000
    >>> my_phone.num_apps
    0
    >>> my_phone.use(10)
    >>> my_phone.charge
    1900
    >>> my_phone.recharge(10)
    >>> my_phone.charge
    2100
    >>> my_phone.install(1000, 'Spotify')
    'App installed'
    >>> my_phone.apps
    {'Spotify'}
    >>> my_phone.storage
    63000
    >>> my_phone.use(210)
    'Out of charge'
    >>> my_phone.recharge(400)
    >>> my_phone.charge
    4000
    >>> my_phone.install(1000, 'Spotify')
    'App already installed'

    # Add your own doctests below
    """
    return

class Phone:
    """
    Implementation of Phone
    """
    
    
    def __init__(self, brand, battery, storage):
        self.brand = brand
        self.battery = battery
        self.storage = storage
        self.charge = battery // 2
        self.charge_rate = 20
        self.num_apps = 0 
        self.apps = set()
        if self.brand == 'Apple':
            self.drain_rate = 10
        elif self.brand == 'OnePlus':
            self.drain_rate = 12
        elif self.brand == 'Samsung':
            self.drain_rate = 8
        else:
            self.drain_rate = 15
    def use(self, minutes): 
        self.charge -= minutes * self.drain_rate
        if self.charge <= 0:
            return "Out of charge"
    def recharge(self, minutes):
        self.charge += minutes * self.charge_rate
        if self.charge > self.battery:
            self.charge = self.battery
            
    def install(self, app_size, app_name):
        if self.charge == 0:
            return 'Out of charge'
        if self.storage < app_size:
            return 'Not enough storage'
        if app_name in self.apps:
            return 'App already installed'
        self.storage -= app_size
        self.num_apps += 1
        self.apps.add(app_name)
        return 'App installed'
      
        
    
    
    pass


############### CLASS PART ##################

# Question 4

def doctests_go_here():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes long with 1220980 streams
    >>> track1.get_artist()
    'Cordae'
    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'
    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True
    
    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False
    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']
    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759
    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA
    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799
    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'
    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'
    >>> play3 = Playlist('test', 'ab')
    >>> play3.get_most_played_song()
    ''
    >>> play3.get_total_streams()
    0
    >>> play3.get_total_length()
    0
    >>> play3.sort_songs('length')
    >>> play3.songs
    []
    >>> play2.combine_playlists(play3)
    True

    >>> TS = Song('Shake it Off', 1.23, '1989', 'Taylor Swift', 12345)
    >>> BC = Song('Halo', 2.34, 'I Am... Sasha Fierce', 'Beyoncé', 23456)
    >>> JB = Song('Baby', 3.45, 'Okay', 'Justin Bieber', 34567)
    >>> LG = Song('Bad Romance', 4.53, 'Talk You Back', 'Lady Gaga', 45678)
    >>> AG = Song('Side to Side', 1.01, 'Dangerous Woman', 'Ariana Grande', 56432)
    >>> SG = Song('BiggieBig', 3.22, 'The Album', 'Selena Gomez', 987)
    >>> WG = Song('God is Fair', 32.43, 'GOD IS AROUND US', 'Windaco God', 99999999)
    >>> BM = Song('Talking to the Moon', 3.38, 'Doo-Wops & Hooligans', 'Bruno Mars', 2814901)
    >>> NB = Song('Long Song', 99999.99, 'Billy Boy', 'Nobody Billy', 7654321)
    >>> Playlist1 = Playlist('God Spoken!', 'Yes sir')
    >>> Playlist2 = Playlist('Do you still love me if I am DJ', 'Xiaozi')
    >>> Playlist3 = Playlist('Best Song', 'Ye')
    >>> lst = [TS,BC,JB,LG,AG,SG,WG,BM,NB]

    """
    return


class Song:
    """
    Implementation of a song
    """
    platform = 'Spotify'

    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song
        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        assert len(name) > 0
        assert length > 0
        assert len(album) > 0
        assert len(artist) > 0
        assert streams >= 0
        self.name = name 
        self.length = length
        self.album = album
        self.artist = artist
        self.streams = streams
        pass


    def get_name(self):
        """ Getter for name attribute """
        return self.name
        pass


    def get_length(self):
        """ Getter for length attribute """
        return self.length
        pass


    def get_album(self):
        """ Getter for album attribute """
        return self.album
        pass


    def get_artist(self):
        """ Getter for artist attribute """
        return self.artist
        pass


    def get_streams(self):
        """ Getter for streams attribute """
        return self.streams
        pass


    def __str__(self):
        """
        String representation of Song
        """
        return f"'{self.name}' by {self.artist} on '{self.album}' is {self.length} minutes long with {self.streams} streams"
        pass


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        return f"Listening to '{self.name}' by {self.artist}"
        pass


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        songs = [song.name for song in playlist.songs]
        if self.name in songs:
            return False
        playlist.songs.append(self)
        return True

# Question 5

class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist
        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist
        Attributes:
        songs (list): list used to store songs in playlist
        """
        self.title = title
        self.user = user
        self.songs = []
        pass


    def get_title(self):
        """ Getter for title attribute """
        return self.title 


    def get_user(self):
        """ Getter for user attribute """
        return self.user
    

    def get_songs(self):
        """ Getter for songs attribute """
        return self.songs


    def __str__(self):
        """
        String representation of Playlist
        """
        return f"Playlist '{self.title}' by {self.user} has {len(self.songs)} songs"



    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        if song in self.songs:
            return False
        self.songs.append(song)
        return True


    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        if song in self.songs:
            self.songs.remove(song)
            return True
        return False


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        if sort_by == 'length':
            self.songs.sort(key=lambda x: x.get_length())
        elif sort_by == 'name':
            self.songs.sort(key=lambda x: x.get_name())
        elif sort_by == 'streams':
            self.songs.sort(key=lambda x: x.get_streams())
        pass


    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        return sum(song.get_streams() for song in self.songs)


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        total_length = sum(song.get_length() for song in self.songs)
        return total_length
        pass


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that records all the songs played.
        If the playlist is empty, return "Empty"
        """
        if not self.songs:
            return "Empty"
        result = ""
        for song in self.songs:
            result += f"Listening to '{song.get_name()}' by {song.get_artist()}\n"
        return result.strip()
    

    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        not_added = sum(1 for song in other_playlist.songs if song in self.songs)
        self.songs.extend(song for song in other_playlist.songs if song not in self.songs)
        return True if not_added == 0 else not_added
    

    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        if not self.songs:
            return ''
        return max(self.songs, key=lambda x: x.get_streams()).get_name()
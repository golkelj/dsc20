"""
DSC 20 Winter 2025, Lab 07
Name: Jaden Goelkel
PID: A18247795
Source: Lecture and Readings
"""

# Question 1
def max_recursion(tup):
    """
    Find the maximum element in a tuple recursively.

    Args:
        tup (tuple): a tuple of integers
    Returns:
        The maximum number

    >>> max_recursion((1,2,3,4))
    4
    >>> max_recursion((13,2,3,4))
    13
    >>> max_recursion((13,2,33,4))
    33
    """
    if len(tup) == 0: 
        return 0
    if len(tup) == 1:
        return tup[0]
    new = max_recursion(tup[1:])
    if new < tup[0]:
        return tup[0]
    else:
        return new

# Question 2
def max_or_min_recursion(tup, find_max = True):
    """
    Find the maximum or minimum element in a tuple recursively.

    Args:
        tup (tuple): a tuple of integers
        find_max (bool): whether to find max or min
    Returns:
        The maximum or minimum number

    >>> max_or_min_recursion((1,2,3,4))
    4
    >>> max_or_min_recursion((13,2,3,4), False)
    2
    >>> max_or_min_recursion((13,2,33,-4), True)
    33
    """
    if len(tup) == 0: 
        return 0
    if len(tup) == 1:
        return tup[0]
    if find_max:
        new = max_or_min_recursion(tup[1:], True)
        if new < tup[0]:
            return tup[0]
        else:
            return new
    elif not find_max:
        new = max_or_min_recursion(tup[1:], False)
        if new > tup[0]:
            return tup[0]
        else:
            return new

# Question 3
def find_winner(record, find_max=True):
    """
    Find the team with highest or lowest score recursively.

    Args:
        record (list): a list of tuples, where the first element in each tuple 
        is the team's name and the second element is the team's score
        find_max (bool): whether to find team with max or min score
    Returns:
        The team with highest or lowest score, and returns first if there is
        a tie

    >>> find_winner([('Red',23),('Green', 49), ('Blue', 32)])
    'Green'
    >>> find_winner([('UCSD', 12.88),('SDSU', 15)], find_max=False)
    'UCSD'
    >>> find_winner([('Panda', 10), ('Koala', 10), ('Hippo', 5)], find_max=True)
    'Panda'
    """
    def helper(i, current):
        if i == len(record):
            return current[0]
        new = record[i]
        if (find_max and new[1] > current[1]) or (not find_max and new[1] < current[1]):
            current = new
        return helper(i + 1, current)
    if not record:
        return None
    return helper(1, record[0])

# Question 4
def from_list_to_dict(lst):
    """
    Converts a list of tuples into a dictionary recursively.

    Args:
        lst (list): a list of tuples, where the first element is the team name 
        (key) and second element is their score (value)
    Returns:
        A dictionary with each team name as keys and their score as values

    >>> lst = [(1,2),(3,4),(5,6)]
    >>> from_list_to_dict(lst)
    {1: 2, 3: 4, 5: 6}

    >>> lst = [("one",1),("two",2)]
    >>> from_list_to_dict(lst)
    {'one': 1, 'two': 2}

    >>> lst = []
    >>> from_list_to_dict(lst)
    {}
    """
    if len(lst) == 0: 
        return {}
    if len(lst) == 1:
        return {lst[-1][0]: lst[-1][1]}
    else:
        new = from_list_to_dict(lst[:-1])
        new[lst[-1][0]] = lst[-1][1]
        return new

# Question 5
class Mascot:
    """ 
    Creates a simple Mascot class with 1 class attribute (type)
    and 3 instance attributes (color, nickname, event)
    >>> mascot1 = Mascot("blue and white", "Shark", "West Athletic Conference")
    >>> Mascot.brings
    'Luck'
    >>> mascot1.color
    'blue and white'
    >>> mascot1.sing_song("Baby Shark")
    "Shark sings 'Baby Shark' at West Athletic Conference"
    >>> mascot1.change_nickname("Doo Doo")
    >>> mascot1.nickname
    'Doo Doo'
    >>> mascot1.event
    'West Athletic Conference'


    >>> mascot2 = Mascot('green', 'Stanford Tree',\
'Collegiate Football Conference')
    >>> Mascot.brings
    'Luck'
    >>> mascot2.color
    'green'
    >>> mascot2.sing_song("Deck the Halls")
    "Stanford Tree sings 'Deck the Halls' at Collegiate Football Conference"
    >>> mascot2.change_nickname("The Tree")
    >>> mascot2.nickname
    'The Tree'
    """
    brings = "Luck"
    
   
 # Initializer (Constructor) / Instance Attributes
    def __init__(self, color, nickname, event):
        self.color = color
        self.nickname = nickname
        self.event = event

    def sing_song(self, song):
        return f"{self.nickname} sings '{song}' at {self.event}"

    def change_nickname (self, new_name):
        self.nickname = new_name



# Question 6
class Game:
    """
    Creates a class with 1 class attribute and two class methods

    >>> Game.mascot
    'King Triton'
    >>> Game.starts()
    'Saturday, November 2'
    >>> Game.ends()
    'Sunday, November 17'
    """
    mascot = "King Triton"
    
    def starts():
        return 'Saturday, November 2'
    
    def ends():
        return 'Sunday, November 17'



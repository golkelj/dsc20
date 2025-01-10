"""
DSC 20 Winter 2025 Homework 01
Name: Jaden Goelkel 
PID: A18247795
"""

# Question 1
def login(fname, lname):
    """
    Creates a login by reversing the first name and the last name then taking
    everyother value of the of the first name then concatinating every 3rd value
    of the lname 
    
    >>> login("Marina", "Langlois")
    'aiaLgi'
    >>> login("", "")
    ''
    >>> login("San", "Diego")
    'nSDg'

    # Add your own doctests below
    >>> login("jaden", "a")
    "ndjfa"
    >>> login("joe,"joe")
    "eje"
    >>> login("","t")
    "t" 
    """
    reversed_fname = fname[::-1]
    reversed_lname = lname[::-1] 
    
    return reversed_fname[0::2] + reversed_lname[0::3]


# Question 2
def ages(age1, age2):
    """
    This function will return the higher value of age1 and age2 
    
    
    >>> ages(19, 21)
    21
    >>> ages(26, 21)
    21
    >>> ages(26, 27)
    'You both can rent!'
    >>> ages(19, 23)
    19

    # Add your own doctests below
    >>> ages(10, 1)
    10 
    >>> ages(11, 12) 
    12 
    >>> ages(5, 3 ) 
    5
    """
    if age1 > age2: 
        return age1 
    return age2


# Question 3
def renter(name1, name2, name3):
    """
    This takes in the name of 3 renters and the return the person with the longest name. If there is multiple names
    with the same lenght it will return the largest name number (ie. name3 is a larger name number than name2)

    >>> renter("K", "BB", "Joy")
    'Joy'
    >>> renter("Joy", "K", "BB")
    'Joy'
    >>> renter("BB", "Joy", "K")
    'Joy'
    >>> renter("BB", "K", "Jo")
    'Jo'
    >>> renter("BB", "Jo", "Su")
    'Su'

    # Add your own doctests below
    >>> renter("K", "BB", "Jaden")
    'Jaden'
    >>> renter("Jaden", "Jaden", "Jaden")
    'Jaden'
    >>> renter("BB", "hh", "doug")
    'doug'
    """
    current_longest_name = name1 
    if len(name2) >= len(name1): 
        current_longest_name = name2
    if len(name3) >= len(current_longest_name): 
        current_longest_name = name3
        
    return current_longest_name


# Question 4.1
def helper_distance(lst, x2, y2):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    
    >>> helper_distance([0, 0], 3, 4)
    5.0
    >>> helper_distance([-3, -4], 3, 4)
    10.0
    >>> helper_distance ([100, 100], 100.5, 100)
    0.5

    # Add your own doctests below
    """
    x1 = lst[0] 
    y1 = lst[1]
    
    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5


# Question 4.2
def lunch(lunch_places, office_x, office_y, threshold):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> lunch([[0, 0], [30.5, 20.7]], 3.2, 4, 6)
    [[0, 0]]
    >>> lunch([[-3, -4], [6, 7]], 3, 4, 10)
    [[-3, -4], [6, 7]]
    >>> lunch ([[100, 100]], 100.5, 100, 0.2)
    []

    # Add your own doctests below
    """
    
    return


# Question 5
def lunch_names(lunch_places, office_x, office_y, threshold, names):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> lunch_names([[0, 0], [30, 20], [5, 9]], 3.2, 4, 6, \
    ['place1', 'place2', 'place3'])
    ['place1', 'place3']
    >>> lunch_names([[-3, -4], [6, 7]], 3, 4, 10, \
    ['place1', 'place2'])
    ['place1', 'place2']
    >>> lunch_names ([[100, 100]], 100.5, 100, 0.2, ['place1'])
    []

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #
    return


# Question 6
def meeting_message(i_name, time, place, s_name):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> print(meeting_message("Penny", "3:15pm", "Cheesecake Factory", \
        "Sheldon"))
    Dear Penny,
    Please join our meeting at 3:15pm, at the Cheesecake Factory.
    <BLANKLINE>
    See you soon: Sheldon

    >>> print(meeting_message("Freya", "", "Dog Park", "Marina"))
    Dear Freya,
    Please join our meeting at , at the Dog Park.
    <BLANKLINE>
    See you soon: Marina

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #
    return


# Question 7
def seat_number(lst):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> seat_number(["Marina", "Tom", "B"])
    [6, 3, 1]
    >>> seat_number(["Marina", "Sue", "Ben", "Freya"])
    [6, 3, 'taken', 5]
    >>> seat_number(["Marina", "Sue", "Ben", ""])
    [6, 3, 'taken', 0]

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #
    return


# Question 8
def computers(choices):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> computers(["DESKtop", "LAPtop", "DESKtop"])
    True
    >>> computers(["LAPtop", "LAPtop"])
    False
    >>> computers(["DESKtop", "Pager", "Tablet", "LAPtop"])
    False

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #
    return


# Question 9
def age_average(lst):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> age_average(["20", "21", "22"])
    '21.0'
    >>> age_average(["50", "25", "30"])
    '35.0'
    >>> age_average(["40", "-999", "45"])
    '42.5'
    >>> age_average([])
    '0.0'

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #
    return


# Question 10
def supervision_teams(team, company_name):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> supervision_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])

    # Add your own doctests below
    """
    # YOUR CODE GOES HERE #
    return
    
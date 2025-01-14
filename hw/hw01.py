"""
DSC 20 Winter 2025 Homework 01
Name: Jaden Goelkel 
PID: A18247795
"""

# Question 1
def login(fname, lname):
    """
    Creates a login by reversing the first name then taking
    everyother value and then adding every 3rd value of the last name
    of the lname
    ---
    Parameters: 
        fname (str): The first name 
        lname (str): The last name 

    ---
    Returns:
        str: The new created name 
    
    >>> login("Marina", "Langlois")
    'aiaLgi'
    >>> login("", "")
    ''
    >>> login("San", "Diego")
    'nSDg'

    # Add your own doctests below
    >>> login("jaden", "a")
    'ndja'
    >>> login("joe", "joe")
    'ejj'
    >>> login("", "")
    ''
    
    """
    reversed_fname = fname[::-1]
    
    
    return reversed_fname[0::2] + lname[0::3]


# Question 2
def ages(age1, age2):
    """   
    Finds the age that is closest to but less than 23 and returns it. If both ages are atleast 23 then returns "You both can rent!". 

    ---
    Parameters: 
        age1 (int): The first age 
        age2 (int): The second age
    ---
    Returns:
        int: the age closer but not over 23, or str: "You both can rent!" 
    
    >>> ages(19, 21)
    21
    >>> ages(26, 21)
    21
    >>> ages(26, 27)
    'You both can rent!'
    >>> ages(19, 23)
    19
    
    # Add your own doctests below
    >>> ages(11, 10)
    11
    >>> ages(11, 12) 
    12
    >>> ages(15, 13) 
    15
    """
    if age1 > 23 and age2 > 23: 
        return "You both can rent!"
    if age1 >= 23: 
        return age2
    if age2 >= 23:
        return age1
    
    if 23 - age1 > 23 - age2: 
        return age2
    return age1


# Question 3
def renter(name1, name2, name3):
    """
    This takes in the name of 3 renters and the return the person with the longest name and the name that is furthest to the right 
    
    ---
    Parameters: 
        name1 (str): The first name 
        name2 (str): The second name 
        name3 (str): The third name
    ---
    Returns:
        str: The longest largest integer name 
        
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
    Find the elcidean distance between 2 points 
    ---
    Parameters: 
        lst (list): Contains 2 floating point numbers 
        x2 (float): x-coordinate of the starting point 
        y2 (float): y-coordinate of the starting point 
    ---
    Returns:
        The elcidean distance 
    
    >>> helper_distance([0, 0], 3, 4)
    5.0
    >>> helper_distance([-3, -4], 3, 4)
    10.0
    >>> helper_distance ([100, 100], 100.5, 100)
    0.5

    # Add your own doctests below
    >>> helper_distance([0, 0], 0, 4)
    4.0
    >>> helper_distance([0, 0], 0, 0)
    0.0
    >>> helper_distance ([100, 100], 101, 100)
    1.0
    """
    x1 = lst[0] 
    y1 = lst[1]
    
    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5


# Question 4.2
def lunch(lunch_places, office_x, office_y, threshold):
    """
    Find the elcidean distance between 2 points 
    ---
    Parameters: 
        lunch_places (list): Contains a list of 2 floating point numbers 
        office_x (float): x-coordinate of the starting point 
        office_y (float): y-coordinate of the starting point
        threshold (float): maximun distance willing to travel 
    ---
    Returns:
        lunch places that are less than or equal to the starting point 
    >>> lunch([[0, 0], [30.5, 20.7]], 3.2, 4, 6)
    [[0, 0]]
    >>> lunch([[-3, -4], [6, 7]], 3, 4, 10)
    [[-3, -4], [6, 7]]
    >>> lunch ([[100, 100]], 100.5, 100, 0.2)
    []

    # Add your own doctests below
    >>> lunch([[0, 0], [30.5, 20.7]], 3.2, 4, 0.0001)
    []
    >>> lunch([[-3, -4], [6, 7]], 3, 4, 0.01)
    []
    >>> lunch ([[100, 100]], 100.5, 100, 200)
    [[100, 100]]
    
    """
    output_list = []
    
    for lunch_place in lunch_places: 
        if helper_distance(lunch_place,office_x, office_y) <= threshold: 
            output_list.append(lunch_place)

    
    return output_list


# Question 5
def lunch_names(lunch_places, office_x, office_y, threshold, names):
    """
    Find lunch places that are close enough to the maximun walking threshold 
    ---
    Parameters: 
        lunch_places (list): Contains a list of 2 floating point numbers 
        office_x (float): x-coordinate of the starting point 
        office_y (float): y-coordinate of the starting point
        threshold (float): maximun distance willing to travel 
        name (list): the name of the restaurant
    ---
    Returns:
        names of lunch places that are less than or equal to the starting point 
        
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
    output_list = []
    i = 0 
    for lunch_place in lunch_places: 
        if helper_distance(lunch_place,office_x, office_y) <= threshold: 
            output_list.append(names[i]) 
        i += 1 
        
    
    return output_list


# Question 6
def meeting_message(i_name, time, place, s_name):
    """
    Takes the name of the invitee, time of day, place and the name of the message creator, as strings. It then returns an invitation, as a string.
    ---
    Parameters: 
        i_name (str): The name of the invitee 
        time (str): The time of the day
        place (str): The location of the event
        s_name (str): The name of the creator
    ---
    Returns:
        The invitation message
        
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
    message = f"Dear {i_name},\nPlease join our meeting at {time}, at the {place}.\n\nSee you soon: {s_name}"
    return message 


# Question 7
def seat_number(lst):
    """
    Assign each person in the list a place to sit. If two people have a name with the same lenght it will assign "taken". 
    ---
    Parameters: 
        lst (list ): A list of all the names
    ---
    Returns:
        list: all the seat assignments
    
    >>> seat_number(["Marina", "Tom", "B"])
    [6, 3, 1]
    >>> seat_number(["Marina", "Sue", "Ben", "Freya"])
    [6, 3, 'taken', 5]
    >>> seat_number(["Marina", "Sue", "Ben", ""])
    [6, 3, 'taken', 0]

    # Add your own doctests below
    """
    seat_list = []
    for name in lst: 
        if len(name) not in seat_list: 
            seat_list.append(len(name))
        else: 
            seat_list.append("taken") 
                
    return seat_list


# Question 8
def computers(choices):
    """
    Counts if DESKtop is written in the list more times than LAPtop. 
    ---
    Parameters: 
        choices (list): list of strings that contains times of computers in the office. 
    ---
    Returns:
        Boolean: True if there is more DESKtops than LAPtops, False if not. 
    
    >>> computers(["DESKtop", "LAPtop", "DESKtop"])
    True
    >>> computers(["LAPtop", "LAPtop"])
    False
    >>> computers(["DESKtop", "Pager", "Tablet", "LAPtop"])
    False

    # Add your own doctests below
    """
    desktop_count = 0 
    laptop_count = 0 
    for choice in choices: 
        if choice == "DESKtop": 
            desktop_count += 1 
        elif choice == "LAPtop":
            laptop_count += 1 
    if desktop_count > laptop_count: 
        return True 
    return False


# Question 9
def age_average(lst):
    """
    Calculates the average age of a friend group. Some people do not want there ages to be included so they will not be counted 
    ---
    Parameters: 
        lst (list): list of ages 
    ---
    Returns:
        float: The average of the ages
        
    >>> age_average(["20", "21", "22"])
    '21.0'
    >>> age_average(["50", "25", "30"])
    '35.0'
    >>> age_average(["40", "-999", "45"])
    '42.5'
    >>> age_average([])
    '0.0'

    # Add your own doctests below
    
    >>> age_average(["50", "-23", "30"])
    '40.0'
    >>> age_average(["40", "-999", "-999"])
    '40.0'
    >>> age_average([0.0])
    '0.0'
    
    
    """
    valid_counts = 0 
    total = 0
    for number in lst: 
        if int(number) > 0: 
            total += int(number)
            valid_counts += 1 
    if valid_counts > 0: 
        return str(total/valid_counts)
    return '0.0'


# Question 10
def supervision_teams(team, company_name):
    """
    Divides a list of participants into two teams based on the position in the index. Team 1 is made up of even number and team 2 is made up of odd numbers. 
    ---
    Parameters: 
        team (list): A list of participants 
        company_name (str): The name of the painting company
    ---
    Returns:
        tuple: The first time  including the company name as the first element and all participants from even indices and the second team including the company name as the last element and all participants from odd indices.
        
    >>> supervision_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])

    # Add your own doctests below
    >>> supervision_teams(["p1", "p2", "p3"], "jaden")
    (['jaden', 'p1', 'p3'], ['p2', 'jaden'])
    >>> supervision_teams(["p1"], "jaden")
    (['jaden', 'p1'], ['jaden'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "jaden")
    (['jaden', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'jaden'])
    """
    
    team1 = [company_name]
    team2 = []
    i = 0 
    for j in team:
        if i % 2 == 0: 
            team1.append(j)
        else: 
            team2.append(j)
        i += 1 
    team2.append(company_name)
    return (team1, team2)
    
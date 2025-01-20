"""
DSC 20 Winter 2024 Homework 02
Name: Jaden Goelkel
PID: A18247795
Source: NA
"""

# Question 1
def name_mapping(given_names, preferred_names):
    """
    description
    --
    Parameters:
        
    --
    Returns:
       

    >>> given_names = ['Amanda', 'Jeffrey', 'Richard']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('Richard', 'Rick')]

    >>> given_names = ['Amanda', 'Jeffrey']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('NO NAME PROVIDED', 'Rick')]

    >>> given_names = []
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('NO NAME PROVIDED', 'Mandy'), ('NO NAME PROVIDED', 'Jeff'), \
('NO NAME PROVIDED', 'Rick')]

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return


# Question 2
def valid_pairs(keys, values):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys =[]
    >>> values =[]
    >>> valid_pairs(keys, values)
    []

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return


# Question 3
def dict_of_names(name_tuples):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> dict_of_names([('Richard', 'Rick'),
    ... ('Roxanne', 'Rose'), ('Roxanne', 'Ann'),
    ... ('Richard', 'Ricky'), ('Roxanne', 'Roxie'),
    ... ('Mitchell', 'Mitch')])
    {'Richard': ['Rick', 'Ricky'], 'Roxanne': ['Rose', 'Ann', 'Roxie'], \
'Mitchell': ['Mitch']}

    >>> dict_of_names([('Melissa', 'Lisa'),
    ... ('Isabel', 'Bella'), ('NO NAME PROVIDED', 'Faith')])
    {'Melissa': ['Lisa'], 'Isabel': ['Bella'], \
'NO NAME PROVIDED': ['Faith']}

    >>> dict_of_names([('NO NAME PROVIDED', 'Derrick'), \
    ('NO NAME PROVIDED', 'Jacob')])
    {'NO NAME PROVIDED': ['Derrick', 'Jacob']}

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return


# Question 4.1
def contractor_payment(suggestions):
    """
     description
    --
    Parameters:
        
    --
    Returns:
       
    >>> contractor_payment([[10, 20, 30], [0, 20, 10]])
    {'1': 5.0, '2': 20.0, '3': 20.0}

    >>> contractor_payment([[10, 20, 30], [30, 20, 10], [5, 10, 15]])
    {'1': 15.0, '2': 16.67, '3': 18.33}

    >>> contractor_payment([[-5, -10, -4], [-20, 15, 40]])
    {'1': -12.5, '2': 2.5, '3': 18.0}

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 4.2
def new_pay(hours):
    """
    description
    --
    Parameters:
        
    --
    Returns:
       
    >>> case1 = {'1': 200, '2': 138, '3': 172}
    >>> round(new_pay(case1), 2)
    0.51
    >>> case1
    {'1': 200, '2': 138, '3': 172, 'pay': 'Bonus'}

    >>> case2 = {'1': 130, '2': 84, '3': -14}
    >>> new_pay(case2)
    -10
    >>> case2
    {'1': 130, '2': 84, '3': -14, 'pay': 'Penalty'}

    >>> case3 = {'1': 42, '2': 96, '3': 63}
    >>> round(new_pay(case3), 1)
    -2.4
    >>> case3
    {'1': 42, '2': 96, '3': 63, 'pay': 'Penalty'}

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 5
def potential_ideas_for_business(items):
    """
     description
    --
    Parameters:
        
    --
    Returns:
       
    >>> items = {'supplier 1': ['Tea', 'Peaches'], \
    'supplier 2': ['Peaches', 'Apples', 'Cups']}
    >>> potential_ideas_for_business(items)
    ['Apples', 'Cups', 'Peaches', 'Tea']

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
    'supplier 2': ['Milk', 'Eggs', 'Vanilla', 'Butter'], \
    'supplier 3': ['Butter', 'Sugar']}
    >>> potential_ideas_for_business(items)
    ['Butter', 'Chocolate', 'Eggs', 'Flour', 'Milk', 'Sugar', 'Vanilla']

    >>> items = {'supplier 1': [], 'supplier 2': []}
    >>> potential_ideas_for_business(items)
    []
    """
    # YOUR CODE GOES HERE #
    return

# Question 6.1
def count_lines_1(filepath):
    """
     description
    --
    Parameters:
        
    --
    Returns:
       
    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return


# Question 6.2
def count_lines_2(filepath):
    """
     description
    --
    Parameters:
        
    --
    Returns:
       
    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return


# Question 6.3
def count_lines_3(filepath):
    """
    description
    --
    Parameters:
        
    --
    Returns:
       
    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return


# Question 7
def collected_items(filepath):
    """
    description
    --
    Parameters:
        
    --
    Returns:
       
    >>> collected_items('files/ings1.txt')
    ['ice-cream', 'boba tea', 'fish']
    >>> collected_items('files/ings2.txt')
    ['shovel', 'headphones', 'bird', 'brownies']
    >>> collected_items('files/empty_trip.txt')
    []

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return


# Question 8
def case_letters(filepath):
    """
    description
    --
    Parameters:
        
    --
    Returns:
       
    >>> case_letters('files/AlErNaTiNg.txt')
    >>> with open('files/AlErNaTiNg.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    5
    13
    >>> case_letters('files/another_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    19

    # Add at least 3 doctests below here #
    >>> case_letters('files/Another_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile3:
    ...    print(outfile3.read().strip())
    1
    18
    >>> case_letters('files/JAden.txt')
    >>> with open('files/another_test.txt', 'r') as outfile4:
    ...    print(outfile4.read().strip())
    2
    3
    >>> case_letters('files/poopoo.txt')
    >>> with open('files/another_test.txt', 'r') as outfile5:
    ...    print(outfile5.read().strip())
    0
    6
    """
    file_name = filepath.split("/")[-1].split(".")[0]
    with open(filepath, "w") as writer:
        writer.writelines([len(i) for i in file_name if i.isupper()])
        writer.writelines(len(file_name) - [len(i) for i in file_name if i.isupper()])
        
    
    return 


# Question 9
def map_office(filepath):
    """
    description
    --
    Parameters:
        
    --
    Returns:
       
    >>> map_office('files/offices1.txt')
    259
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    not a valid office number
    second floor

    >>> map_office('files/offices2.txt')
    734
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    third floor and above
    not a valid office number
    second floor
    ground floor
    """
    # YOUR CODE GOES HERE #
    return




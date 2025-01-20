"""
DSC 20 Winter 2024 Homework 02
Name: Jaden Goelkel
PID: A18247795
Source: NA
"""

# Question 1
def name_mapping(given_names, preferred_names):
    """
    Takes two lists and then adds a tuple to a list that contains the given \
    name and the preferred name. If no given name is given then "NO NAME \
    PROVIDED" is added. 
    --
    Parameters:
        given_name (list): List of the given names
        preferred_names (list): List of the preferred names
        
    --
    Returns:
        list: List of the tuples of the given names and the preferred names \
       

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
    >>> given_names = [] 
    >>> preferred_names = []
    >>> name_mapping(given_names, preferred_names)
    []
    >>> given_names = ['jaden']
    >>> preferred_names = ['Jaden']
    >>> name_mapping(given_names, preferred_names)
    [('jaden', 'Jaden')]
    >>> given_names = []
    >>> preferred_names = ['Jaden']
    >>> name_mapping(given_names, preferred_names)
    [('NO NAME PROVIDED', 'Jaden')]
    
    """
    output = []
    if given_names == None:
        return []
    i = 0
    for name in preferred_names:
        if i > len(given_names)-1:
            output.append(("NO NAME PROVIDED", name))
        else: output.append((given_names[i], name))
        i += 1
        
    return output

# Question 2
def valid_pairs(keys, values):
    """
    Creates dictionary key-values pair if the inputs are valid, if not \
    if not it will create a tuple with the string 'not valid' 
    --
    Parameters:
        keys (list): A list of a variety of data types
        values (list): A list of a variety of data types
        
    --
    Returns:
        list: list of tuples with the key-value pairs
    

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
    >>> keys =['j']
    >>> values =['a']
    >>> valid_pairs(keys, values)
    [('j', 'a')]
    >>> keys =['ja']
    >>> values =['de']
    >>> valid_pairs(keys, values)
    [('ja', 'de')]
    >>> keys =['jaden']
    >>> values =['goelkel']
    >>> valid_pairs(keys, values)
    [('jaden', 'goelkel')]
    """
    i = 0
    dict_list = []
    for key in keys:
        if isinstance(key, (str, int, tuple, float)):
            dict_list.append((key, values[i]))
        else: dict_list.append(("not valid",))
        i += 1

    return dict_list


# Question 3
def dict_of_names(name_tuples):
    """
    Convert a list of the given names and the preferred names to tuples then \
    to a dictionary where keys are given names and values are lists of \
    preferred names.
    --
    Parameters:
    data (list of tuples): A list of the given name and preferred name \
    tuples.

    --
    Returns:
    dict: A dictionary where keys are given names and values are lists of \
    preferred names.
    

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
    >>> dict_of_names([("j", "jadn")])
    {'j': ['jadn']}

    >>> dict_of_names([("ja", "jaden"), ("j", "jaden")])
    {'ja': ['jaden'], 'j': ['jaden']}

    >>> dict_of_names([("jad", "jaden")])
    {'jad': ['jaden']}
    """
    name_dict = {}
    for name in name_tuples:
        if name[0] in name_dict:
            name_dict[name[0]].append(name[1])
        else:
            name_dict[name[0]] = [name[1]]
        
    return name_dict


# Question 4.1
def contractor_payment(suggestions):
    """
    Calculates the average payment for the contractors based on the provided \
    list of suggestions.
    --
    Parameters:
    payments (list): A list of lists, where each inner list contains payment\
    suggestions for the three contractors.

    --
    Returns:
    dict: A dictionary with the contractor labels ('1', '2', '3'),\
    and the values are the average payments for each contractor.
    
       
    >>> contractor_payment([[10, 20, 30], [0, 20, 10]])
    {'1': 5.0, '2': 20.0, '3': 20.0}

    >>> contractor_payment([[10, 20, 30], [30, 20, 10], [5, 10, 15]])
    {'1': 15.0, '2': 16.67, '3': 18.33}

    >>> contractor_payment([[-5, -10, -4], [-20, 15, 40]])
    {'1': -12.5, '2': 2.5, '3': 18.0}

    # Add at least 3 doctests below here #
    >>> contractor_payment([[1, 2, 3], [0, 2, 1]])
    {'1': 0.5, '2': 2.0, '3': 2.0}

    >>> contractor_payment([[100, 200, 300], [300, 200, 100], [50, 100, 150]])
    {'1': 150, '2': 166.7, '3': 183.3}

    >>> contractor_payment([[0, 0, 0], [0, 0, 0]])
    {'1': 0.0, '2': 0.0, '3': 0.0}
    """
    contr_1, contr_2, contr_3 = 0.0, 0.0, 0.0 
    suggestions_dict = {}
    for payment in suggestions:
        contr_1, contr_2, contr_3 = contr_1 + payment[0], \
            contr_2 + payment[1], contr_3 + payment[2]
        
    suggestions_dict['1'] = contr_1/ len(suggestions)
    suggestions_dict['2'] = contr_2/ len(suggestions)
    suggestions_dict['3'] = contr_3/ len(suggestions)
    
    return suggestions_dict

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
    >>> case_letters('files/nother_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile3:
    ...    print(outfile3.read().strip())
    0
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
    uppercase_count = len([i for i in file_name if i.isupper()])  # Count uppercase letters
    lowercase_count = len(file_name) - uppercase_count   
    with open(filepath, "w") as writer:
        writer.writelines(str(uppercase_count) + "\n")
        writer.writelines(str(lowercase_count) + "\n")
        
    
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




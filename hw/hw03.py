"""
DSC 20 Winter 2024 Homework 03
Name: Jaden Goelkel
PID: A18247795
Source: Readings
"""
# Question 1.1
def operate_nums(lst):
    """
    For numbers in a list it will double of the odd integers and triple all of the even integers  
    --
    Parameters:
        lst (list): 
        
    --
    Returns:
        list: All odd numbers doubled and even numbers tripled
    

    >>> operate_nums([1, 2, 3, 's'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3.1, -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3, -2, 0, 5])
    [6, 6, -6, 0, 10]
    >>> operate_nums([1, 2, 'f', 's'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, "chich", -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([1, 3, -2, 0, 5])
    [2, 6, -6, 0, 10]
    """
    assert all([isinstance(i, int) for i in lst]) 
    double =  2
    triple = 3
    new_list = [i * triple if i % 2 == 0 else i * double for i in lst]
    return new_list

# Question 1.2
def string_lengths(text, nums):
    """
    Takes a list of text and number and check for each index position that \
    that the len of the text is greater than the num at the same index
    --
    Parameters:
        text (list): list of non empty strings that are going to be used for \
        the comparsion
        nums (list): list of positive integers 
        
    --
    Returns:
        list: list of booleans that is True if the lenght of the text at i is\
        greater than the positive integer at i
    
    >>> string_lengths(['a', 'b', 'c'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['', 'abc'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['a', 'b'], [-1, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['abc', 'abcd', 'abcde'], [2, 5, 5])
    [True, False, False]
    
    ###my tests###
    >>> string_lengths([], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths([''], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['', ''], [-1, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert all(isinstance(i, int) and i > 0 for i in nums)
    assert all(isinstance(i, str) and len(i) > 0 for i in text)
    assert len(text) == len(nums)
    return [len(text[i]) > nums[i] for i in range(len(nums))]

# Question 1.3
def process_dict(input_dict):
    """
    Calculates the len of the number in the keys tuple and the sum of the \
    len of the values for each element of the dictionary
    --
    Parameters:
        input_dict (dict): Keys are tuples of integers and the values are \
        a list of strings 
    --
    Returns:
        list: list with each item being the sum of the \
        length of all the values and len of the keys \
        tuple 
    
    >>> process_dict({1: ['a', 'b', 'c'], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['a', 0], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['dsc', 'dsc20', 'dsc30'], (2,): \
    ['b']})
    [15, 2]
    
    ###My tests###
    >>> process_dict({1: [5], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): [6.53], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): [100000], (2,): \
    ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert (all([isinstance(i, tuple) for i in input_dict.keys()]) 
            and all(all(isinstance(i, str) for i in j) for j in 
                     input_dict.values()))
    return [len(j) + sum(len(i) for i in input_dict[j]) for j in 
            input_dict.keys()]

# Question 2
def unusual_sort(indices, items):
    """
    Sorts a list of indices and items to give the element, the original\
    index and the new index
    --
    Parameters:
        indices (list) - list of length n that contains integers 0 to n-1
        items (list) - list of length n
        
    --
    Returns:
        list: list of tuples that contains the element from items and the \
        original index from indices and the new index 
    
    >>> unusual_sort([0, 4, 2, 3, 1], \
        ["zero", "four", "two", "three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), \
('three', 3, 3), ('four', 1, 4)]

    >>> unusual_sort([0.0, 4.0, 2.0, 3.0, 1.0], \
    ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3, 0], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError
    
    ##my test##
    >>> unusual_sort([0.0, 4.0, 2.0, 3.0, 1.0], \
    ["zero", "four", "chicken", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3, 0], \
        ["zero", "four", "corn", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3], \
        ["zero", "four", "poo", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError
    
    """
    assert all(isinstance(i, int) for i in indices)
    assert all(i in indices for i in range(len(indices)))
    indexs = [items[i] for i in indices]
    
    return [(indexs[i], indices[i], i)for i in range(len(indices))]

# Question 3
def change_input(strange_list):
    """
    Decodes a list of strings by performing the following transformations on \
    each string, all digits multipled by two, Lowercase vowels converted to\
    uppercase, and all other characters remain unchanged.
    
    Parameters:
        strings (list): list of strings to be decoded
    
    Returns:
        list: list of the new strings with the decoding rules
    
    >>> change_input(["3.14IS PIE", "11My aGe iS"])
    ['6.28IS PIE', '22My AGE IS']
    >>> change_input(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO t12O slEEp At ', '10I lIkE tO stArt wOrk bEfOrE ']
    >>> change_input("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    
    ###my test###
    >>> change_input(["1.14IS PIE", "1My aGe iS"])
    ['2.28IS PIE', '2My AGE IS']
    >>> change_input(["go to sleep at ", \
        "jaden"])
    ['gO tO slEEp At ', 'jAdEn']
    >>> change_input("hello")
    Traceback (most recent call last):
    ...
    AssertionError
     
    """
    digit = '0123456789'
    assert isinstance(strange_list, list) 
    return [''.join(str(int(i) * 2) if i in digit else i.upper()
            if i in ['a','e','i','o','u'] else i for i in j) for j in 
            strange_list]

# Question 4
def change_input_even_more(strange_list):
    """
    Takes a list of and applies the following modifications: Multiple any \
    numbers by 2 and move it to the end of the string, lowercase vowels are\
    turned into uppercase, and everything else is left the same
        
    --
    Parameters:
        strange_list (list): list of strings to be modified
        
    --
    Returns:
        list: list with all the aforementioned modifications
    
    >>> change_input_even_more(["3.14IS PIE", "11My aGe iS"])
    ['.IS PIE628', 'My AGE IS22']
    >>> change_input_even_more(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO tO slEEp At 12', 'I lIkE tO stArt wOrk bEfOrE 10']
    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError

    # Add at least 3 doctests below here #
    >>> change_input_even_more(["31", "12My aGe iS"])
    ['62', 'My AGE IS24']
    >>> change_input_even_more(["my name is jaden", \
        "33"])
    ['my nAmE Is jAdEn', '66']
    >>> change_input_even_more("oo")
    Traceback (most recent call last):
    ...
    AssertionError
    """
    
    assert isinstance(strange_list, list) 
    assert all(isinstance(i, str) for i in strange_list)
    doubler = 2 
    digits = "1234567890"
    
    return [''.join([i.upper() if i in 'aeiou' else i for i in j if i not 
                     in digits]) +  ''.join([str(int(i) * doubler) for i 
                     in j if i in digits]) for j in strange_list]

    

# Question 5.1
def cheapest_gas(gas_stations, mileage):
    """
    Gives the name of the lowest price gas station that is reachable
    --
    Parameters:
        gas_stations (dict): dict with the brands as the key and \
        a tuple as the value with the first element of the tuple \
        being the distance and the second being the cost
        mileage (int): the remaining distance the car can travel \
        to the gas station
        
    --
    Returns:
        string: name of the cheapest gas station within the distance
        
    
    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.3), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_gas(gas_stations, 20)
    'Shell'

    # Add at least 3 doctests below here #
    """
   
    gas_price = [[(i[1], j) for i in gas_stations[j] if i[0] <= mileage] for j in gas_stations]
    gas_price = [i for i in gas_price if len(i) > 0]
    lowest_price = min([i[0] for i in gas_price])
    
    return lowest_price[1]

# Question 5.2
def cheapest_average_gas(gas_stations, mileage):
    """
    Calculates the new pay for the contractors according to the following \
    rules: Contractor 1 hours * 0.1, Contractor 2 hours * 0.15, \
    min(0.02 * abs(100 - hours worked by contractor 3), 0.025 * \
    hours worked by contractor 3) - 5
    --
    Parameters:
        hours (dict): Dictionary containing the hours that each of the \
        contractors worked. 
        
    --
    Returns:
        float: The calculated bonus pay
    
    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.1), (10, 5.4)] \
    }
    >>> cheapest_average_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 20)
    'Shell'

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 6
def new_orders(orders, action, dish_name, amount):
    """
    From a dictionary of orders with a dish and amount pair, it will either \
    of remove items from a certain dish name by a given amount
    --
    Parameters:
        orders (dict): Contains the food items as the keys and the \
        amount as the value
        action (string): "add" or "remove"
        dish_name (string): the name of the dish (already in orders) that \
        the action will be commited onto
        amount (int): the amount that will be added or subtracted to \
        the dish in the orders dictionary
        
    --
    Returns:
        dict: the updated orders dictionary
        
    
    >>> orders = {'pizza': 10, 'burger': 5}
    >>> new_orders(orders, 'add', 'pizza', 5)
    {'pizza': 15, 'burger': 5}

    >>> new_orders(orders, 'remove', 'burger', 3)
    {'pizza': 10, 'burger': 2}

    >>> new_orders(orders, 'remove', 'pizza', 15)
    {'pizza': 0, 'burger': 5}

    >>> new_orders([], 'remove', 'burger', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add at least 3 doctests below here #
    >>> orders = {'pizza': 1, 'burger': 0}
    >>> new_orders(orders, 'add', 'pizza', 5)
    {'pizza': 6, 'burger': 0}

    >>> new_orders(orders, 'remove', 'burger', 3)
    {'pizza': 1, 'burger': 0}

    >>> new_orders(orders, 'remove', 'pizza', 15)
    {'pizza': 0, 'burger': 0}

    >>> new_orders([], 'remove', 'burger', 3)
    Traceback (most recent call last):
    ...
    AssertionError
    
    
    """
    assert isinstance(orders, dict)
    assert isinstance(amount, int)
    assert action == "remove" or action == "add"
   
    return  {dish: max(orders[dish] + amount if action == "add" and
                       dish == dish_name else orders[dish] - amount if
                       action == "remove" and dish == dish_name else
                       orders[dish], 0) for dish in orders}

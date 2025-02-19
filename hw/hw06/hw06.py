"""
DSC 20 Winter 2025 Homework 06
Name: Jaden Goelkel
PID: A18247795
Source: Lecture slides and readings
"""

#Question 1
def randomize(*args):
    """ 
    This function takes any number of arguments and categorizes them into a \
    dictionary based on their type. It processes strings, integers, floats, \
    lists, and other types differently.

    >>> randomize(1, 2.3, False, 'DSC20')
    {'int': [False], 'float': [2], 'garbage': [False], 'str': ['DC0']}
    >>> randomize(True, 4, 'ABC', -9.8, [1,2,3], 'a', False)
    {'garbage': [True, False], 'int': [True], 'str': ['AC', 'a']\
, 'float': [9.8], 'list': [3]}
    >>> randomize(False, True, 'DS', True, 'abc', -3.2, 5, {'a': 1}, -2, ' .')
    {'garbage': [False, True, True, {'a': 1}], 'str': ['D', 'ac', ' ']\
, 'float': [3.2], 'int': [False, True]}
    >>> randomize()
    {}
    >>> randomize(True)
    {'garbage': [True]}

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    # 1
    >>> randomize(3, 4.5, 'hello', [1, 2], None)
    {'int': [False], 'float': [4], 'str': ['hlo'], 'list': [2], 'garbage':\
 [None]}
    
    # 2
    >>> randomize('abcdef', 10, -3.14, [3, 4, 5], True)
    {'str': ['ace'], 'int': [True], 'float': [3.14], 'list': [3], 'garbage':\
 [True]}
    
    # 3
    >>> randomize(0, 'xyz', -2.23, [], False)
    {'int': [True], 'str': ['xz'], 'float': [2.23], 'list': [0], 'garbage':\
 [False]}
    
    """
    everyother = 2
    even_mod = 2
    dict_out = {}
    for i in args:
        if isinstance(i, bool):
            key = 'garbage'
            value = i
        elif isinstance(i, str):
            key = 'str'
            value = i[::everyother]
        elif isinstance(i, int):
            key = 'int'
            value = i % even_mod == 0
        elif isinstance(i, float):
            key = 'float'
            value = int(i) if i > 0 else abs(i)
        elif isinstance(i, list):
            key = 'list'
            value = len(i)
        else:
            key = 'garbage'
            value = i
        if key in dict_out:
            dict_out[key].append(value)
        else:
            dict_out[key] = [value]
    return dict_out
            
        

#Question 2
def rearrange_args(*args, **kwargs):
    """
    This function takes args and kwargs and then creates a list of tuples\
    with either the positonal index of the args of the keyword number and\
    name, then the values as the second item in the tuple
    
    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    #1
    >>> rearrange_args()
    []

    #2
    >>> rearrange_args(1, 2, 3, 4)
    [('positional_0', 1), ('positional_1', 2), ('positional_2', 3), \
('positional_3', 4)]

    #3
    >>> rearrange_args(z=100, a=200, b=300)
    [('keyword_0_z', 100), ('keyword_1_a', 200), ('keyword_2_b', 300)]
    """
    def arg_process(i, args):
        """
        Processes the args with recursion
        """
        if not args:
            return []
        return ([(f"positional_{i}", args[0])] + 
                arg_process(i + 1, args[1:]))
    
    def kwarg_process(i, kwargs):
        """
        Processes the kwargs with recursion
        """
        if not kwargs:
            return []
        key, value = list(kwargs.items())[0]  
        new_kwargs = dict(list(kwargs.items())[1:])
        return [(f"keyword_{i}_{key}", value)] + \
               kwarg_process(i + 1, new_kwargs)
    return arg_process(0, args) + kwarg_process(0, kwargs)

#Question 3.1
def count_the_password(lst, password):
    """
    Compute how many times the password appears in the list

    >>> count_the_password(["cooldragon", "dragon", "gold"], "dragon")
    1
    >>> count_the_password(["DRAGON", "dragon!!"], "dragon")
    0
    >>> count_the_password([], "dragon")
    0
    >>> count_the_password(["dragon "], "dragon")
    0
    >>> count_the_password(["dragon", "likes", "recursions", "right", \
"dragon", "?"], "dragon")
    2

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    # 1
    >>> count_the_password(["dragon", "notdragon", "dragon"], "dragon")
    2

    # 2
    >>> count_the_password(["dragon", "DRAGON", "dragon"], "dragon")
    2

    # 3
    >>> count_the_password(["dragonpoo", "dragon", "dragondragon"], "dragon")
    1

    """
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        if lst[0] == password:
            return 1
        else:
            return 0
    n = 1 if lst[0] == password else 0
    return n + count_the_password(lst[1:], password)

#Question 3.2  
def corrupt_password(input, to_insert):
    """
    Takes an input string add adds an insert after every char. 

    >>> corrupt_password('dragon', '#')
    'd#r#a#g#o#n#'
    >>> corrupt_password('', '@')
    ''
    >>> corrupt_password('I can help', '-')
    'I- -c-a-n- -h-e-l-p-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_password('password', '*')
    'p*a*s*s*w*o*r*d*'
    >>> corrupt_password('test', '!')
    't!e!s!t!'
    >>> corrupt_password('123', '+')
    '1+2+3+'
    """
    if len(input) == 0:
        return ''
    n = input[0]
    return n + to_insert + corrupt_password(input[1:], to_insert)

# Question 3.3
def outsmart_dragon(lst, password, to_insert):
    """
    goes throught list of string and inserts char after every char   \
    in the string or just leaves the string as is if it matches the  \
    password and creates a new list with all the modified/unmodified \
    values

    >>> outsmart_dragon(['dragon'], 'dragon','#')
    ['dragon']
    >>> outsmart_dragon([], 'dragon','@')
    []
    >>> outsmart_dragon(['help me', 'dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'dragon']
    >>> outsmart_dragon(['help me', 'dear dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'd-e-a-r- -d-r-a-g-o-n-']
    >>> outsmart_dragon(['DrAgOn', 'Dragon'], 'dragon','-')
    ['D-r-A-g-O-n-', 'D-r-a-g-o-n-']
    
    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> outsmart_dragon(['test', 'dragon'], 'dragon', '*')
    ['t*e*s*t*', 'dragon']
    >>> outsmart_dragon(['password', 'dragon'], 'dragon', '!')
    ['p!a!s!s!w!o!r!d!', 'dragon']
    >>> outsmart_dragon(['123', 'dragon'], 'dragon', '+')
    ['1+2+3+', 'dragon']
    """
    if len(lst) == 0:
        return []
    
    if lst[0] == password:
        n = [lst[0]]
    else:
        n = [corrupt_password(lst[0], to_insert)]
    return n + outsmart_dragon(lst[1:], password, to_insert)

#Question4
def corrupt_with_vowels(input):
    """
    This function removes all vowels from the input string.

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '
    
    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_with_vowels('hello world')
    'hll wrld'
    >>> corrupt_with_vowels('python programming')
    'pythn prgrmmng'
    >>> corrupt_with_vowels('aeiou')
    ''
    """
    if not input:
        return ''
    if input[0] in 'aeiouAEIOU':
        return corrupt_with_vowels(input[1:])
    else:
        return input[0] + corrupt_with_vowels(input[1:])

#Question 5
def where_to_go(point1, point2, separator):
    """
    returns a strings based on the following:
    -if point1 > point2, then return a string with all int descending between \
    point1 and point2, and the separator inbetween them. 
    -if point1 < point2, then return a string with all int ascending between \
    point2 and point1, and the separator inbetween them.  
    -if the same number, simply return the given number. 

    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> where_to_go(5, 10, '-')
    '5-6-7-8-9-10'
    >>> where_to_go(10, 5, '->')
    '10->9->8->7->6->5'
    >>> where_to_go(3, 3, ',')
    '3'
    """
    if point1 == point2:
        return str(point1)
    if point1 > point2:
        n = point1
        return str(n) + separator + where_to_go(point1 - 1, point2, separator)
    if point2 > point1:
        n = point1
        return str(n) + separator + where_to_go(point1 + 1, point2, separator)
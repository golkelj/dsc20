def switch(dict):
    """_summary_

    Args:
        dict (_type_): _description_
    >>> switch({1:3, 4:1, 5:1})
    {3: 1, 1: 5}
    """
    new_dict = {}
    for i in dict.keys():
        n = dict[i] # values 
        new_dict[n] = i # i is the key and the other is the value 
    return new_dict

# (5 points) Write a higher-order function named match that takes 2 numbers as argu-
# ments. It then returns a function that takes two functions as arguments and returns

# True if the outputs are the same for the functions, False otherwise.
def add(x, y):
    return x+y
def diff (x, y):
    return x-y
def match(x, y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_
        
    >>> match(4, 0)(add, diff)
    True
    >>> match(4, 4)(add, diff)
    False
    """
    def compare(f1, f2): 
        return f1(x, y) == f2(x, y)
    
    return compare
        
def special_ints(cond, n):
    # Print out all integers 1.. i .. n where cond(i) is true
    """
    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> special_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n+1): 
        if cond(i) == True: 
            print(i) 
   
        
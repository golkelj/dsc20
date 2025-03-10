"""
DSC 20 Winter 2025 Homework 09
Name: Jaden Goelkel
PID: A18247795
Source: lecture notes and slides
"""

# Question 1
def question_1():
    """
    1 if a method mutates an object 
	0 otherwise

	>>> answer = question_1()
	>>> len(answer) == 10
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer])
	False
    """
    # YOUR CODE GOES HERE #
    return [0, 0, 0, 1, 1, 0, 0, 1, 1, 1]


# Question 2
def question_2():
    """
    1 if a method is in place
	0 otherwise

	>>> answer = question_2()
	>>> len(answer)==5
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer ])
	False
    """
    # YOUR CODE GOES HERE #
    return [1, 1, 1, 0, 1]


# Question 3
def reverse_list(lst):
    """ 
    Reverse the lists only by mutating the objects

    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]

    # Add at least 3 doctests below here #
     >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]
     >>> x = [1,2]
    >>> reverse_list(x)
    >>> x
    [2, 1]
     >>> x = [1,2,3]
    >>> reverse_list(x)
    >>> x
    [3, 2, 1]
    
    """
    left = 0 
    right = len(lst) - 1 
    
    while left < right: 
        lst[left], lst[right] = lst[right], lst[left]
        left += 1 
        right -= 1 
    return None


# Question 4
def swap_lists(alist1, alist2):
    """
    swaps two list of the same size with each other in place

    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]

    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]

    # Add at least 3 doctests below here #
    >>> list1 = []
    >>> list2 = []
    >>> swap_lists(list1, list2)
    >>> print(list1)
    []
    >>> print(list2)
    []
    
    >>> list1 = [10, 20]
    >>> list2 = [30, 40]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 40]
    >>> print(list2)
    [10, 20]
    
    >>> list1 = [11, 21]
    >>> list2 = [31, 41]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [31, 41]
    >>> print(list2)
    [11, 21]
    
    """
    for i in range(len(alist2)):
        alist1[i], alist2[i] = alist2[i], alist1[i]
    return 
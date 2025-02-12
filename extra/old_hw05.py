"""
DSC 20 Winter 2025 Homework 05
Name: Jaden Goelkel
PID: A18247795
Source: Lecture and readings 
"""

# Question 1

def get_qualified_customers(data, max_avg, min_range):
    """
    Filters the customers based on their data and the input filtering values \
    of the max average and the minimun range 

    >>> data = { \
        "Jayden": [10, 10, 10, 10, 10], \
        "Terry": [1, 2, 3, 4, 5, 6, 7, 8], \
        "Austin": [10, 11, 12, 13, 14], \
        "Noah": [2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 11, 5)
    ['Terry']

    >>> data = { \
        "Caleb": [0, 1, 2, 3, 4, 5], \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, 9, 2)
    ['Caleb', 'Keenan', 'Rome']

    # Add at least 3 doctests below here #
    #1 
    >>> data = { \
        1 : [10, 10, 10, 10, 10], \
        "Terry": [1, 2, 3, 4, 5, 6, 7, 8], \
        "Austin": [10, 11, 12, 13, 14], \
        "Noah": [2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 11, 5)
    Traceback (most recent call last):
    ...
    AssertionError
    
    #2 
    >>> data = { \
        "Caleb": [0, "jaden", 2, 3, 4, 5], \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, 9, 2)
    Traceback (most recent call last):
    ...
    AssertionError
    
    #3
    >>> data = []
    >>> get_qualified_customers(data, 11, 5)
    Traceback (most recent call last):
    ...
    AssertionError
    
    """
    assert isinstance(data, dict) 
    assert all(isinstance(i[0], str) and isinstance(i[1], list)
               for i in data.items())
    assert all(isinstance(j[1], list) and (not j[1] or 
               all(isinstance(i, int) 
               for i in j[1])) for j in data.items())
    avgs = lambda x: sum(x) / len(x) if len(x) > 0 else 0
    ranges = lambda x: max(x) - min(x) if len(x) > 1 else 0
    filtered_keys = list(filter(lambda x: avgs(x[1]) <= max_avg and
                           ranges(x[1]) >= min_range and
                           len(set(x[1])) == len(x[1]), data.items()))

    return [i[0] for i in filtered_keys]


# Question 2

def message_to_customers(customer_file, decision, message):
    """
    Reads a file with company_name,person_in_charge,email,decision and with \
    the information it will create a message to individuals if they qualify,\
    or skip them if they do not 
    
    >>> msg = "unfortunately we cannot work with you."
    >>> message_to_customers("files/customers.txt", "w", msg)
    ['(to: steve@apple.com) Dear Steve at Apple, \
unfortunately we cannot work with you.', \
'(to: jensen@nvidia.com) Dear Jensen at NVIDIA, \
unfortunately we cannot work with you.']

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers.txt", "s", msg)
    ['(to: jeff@amazon.com) Dear Jeff at Amazon, \
we are excited to work with you!', \
'(to: mark@fb.com) Dear Mark at Facebook, \
we are excited to work with you!']

    # Add at least 3 doctests below here #
    """
    output_message = []
    assert isinstance(message, str) 
    assert decision == 's' or decision == 'w'
    with open(customer_file, 'r' ) as reader:
        for i in reader:  
            company_name, person, email, decisions = i.split(',')
            if decisions.strip() == decision: 
                output_message.append(f"(to: {email}) Dear {person} at "
                                      f"{company_name}, {message}")        
    return output_message
            
        
        
            


# Question 3

def forge_votes(vote_file):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> forge_votes("files/vote1.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Patrick,1
    Travis,0
    Clyde,1
    Andy,1

    >>> forge_votes("files/vote2.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,0

    >>> forge_votes("files/vote3.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Andy,1

    # Add at least 3 doctests below here #
    """
    middle_prop = 0.5
    forged_votes = []
    middle_divisor = 2
    forged = ''
    
    with open(vote_file, "r") as reader:
        with open("files/forged.txt", "w") as writer:
            lines = [i.strip().split(",") for i in reader] 
            names = [i[0] for i in lines]
            votes = [i[1] for i in lines]
            num_votes = len(lines)
            current = sum(list(map(lambda x: int(x), votes)))
            if current / num_votes > middle_prop:
                forged = ''.join(f"{names[i]},{votes[i]}\n" for i 
                                in range(len(votes)))
                writer.write(forged)
                return 
            needed_votes = ((num_votes // middle_divisor) + 1) - current
            forged_votes = list(''.join(votes).replace("0","1", needed_votes))
            forged = ''.join(f"{names[i]},{forged_votes[i]}\n" for i 
                            in range(len(forged_votes)))
            writer.write(forged)
            writer.close()
            
            


# Question 4

def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function. No new doctests required.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (True/False) #
    return [True, False, False, True, ..., ..., ..., ..., ..., ...]
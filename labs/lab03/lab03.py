"""
DSC 20 Winter 2025 Lab 03
Name: Jaden Goelkel
PID: A18247795
"""

# Problem 1.1
def keep_a_secret(filename):
    """
    Decodes message from the given input file.

    >>> print(keep_a_secret('files/encoded_1.txt').strip())
    jack reacher
    23@4 b#l31oo%m@^ way
    FSD@si%m3~on fis#he%r
    121 rockefeller avenue
    32'1 fulleH##r "dr^i~v@e
    @@4:)5#0p1m#
    7/29 06.45
    >>> print(keep_a_secret('files/encoded_2.txt').strip())
    kurt hendricks
    simon 1p@egg
    @kremlin office
    b%i>%g@ be>n @lond#o&&n
    moscow
    @reykj@av>>ik:/
    12:50 23/11
    >>> print(keep_a_secret('files/encoded_3.txt').strip())
    <BLANKLINE>
    >>> keep_a_secret('files/encoded_4.txt').strip()
    'kurt hendricks\\nsimon 1p@egg'
    """
    new_string = ''
    with open(filename, "r") as reader: 
        for line in reader: 
            line = line.strip()
            line = line.replace("!", "")
            line = line.replace("?", "")
            line = line.replace(";", "")
            line = line.replace("$", "")
            new_string += line + '\n'
    return new_string


# Problem 1.2
def skipped_lines(filename, skip):
    """
    Decodes message from the given input file by skipping some lines

    >>> print(skipped_lines('files/encoded_1.txt', 1).strip())
    jack reacher
    FSD@si%m3~on fis#he%r
    32'1 fulleH##r "dr^i~v@e
    7/29 06.45
    >>> print(skipped_lines('files/encoded_2.txt', 2).strip())
    kurt hendricks
    b%i>%g@ be>n @lond#o&&n
    12:50 23/11
    >>> print(skipped_lines('files/encoded_3.txt', 1).strip())
    <BLANKLINE>
    >>> skipped_lines('files/encoded_4.txt', 0).strip()
    'kurt hendricks\\nsimon 1p@egg'
    """
    i = 0
    output = ''
    with open(filename, "r") as reader:
        for line in reader:
            if i % (skip + 1) == 0: 
                line = line.strip()
                line = line.replace("!", "")
                line = line.replace("?", "")
                line = line.replace(";", "")
                line = line.replace("$", "")
                output += line + '\n'
            i += 1 
    return output


# Problem 2.1
def loose_change(lst):
    """
    Converts each integer to dollars and cents format

    >>> loose_change([200, 456])
    ['2 dollar(s) and 0 cents', '4 dollar(s) and 56 cents']
    >>> loose_change([9])
    ['0 dollar(s) and 9 cents']
    >>> loose_change([])
    []
    >>> loose_change([7, 77, 777, 7777])
    ['0 dollar(s) and 7 cents', '0 dollar(s) and 77 cents', '7 dollar(s) \
and 77 cents', '77 dollar(s) and 77 cents']
    """
    
    cents = 0 
    dollar = 0 
    output = [] 
    for i in lst:
        cents = i % 100 
        if i >= 100: 
            dollar = (i - cents) / 100 
        output.append(str(int(dollar)) + ' dollar(s) and ' + str(int(cents)) + ' cents') 
    return output

# Problem 2.2
def ignore_cents(lst):
    """
    >>> ignore_cents([20, 46, 24])
    0
    >>> ignore_cents([])
    0
    >>> ignore_cents([120, 746, 3224, 15])
    40
    """
    hundred_divisor = 100
    total = 0 
    for i in lst:
        if i >= hundred_divisor: 
            total += i // hundred_divisor
    return total
    


# Problem 2.3
def ignore_cents_and_small_amount(lst):
    """
    Finds total of changes, ignoring those less than $50 and cents

    >>> ignore_cents_and_small_amount([34, 245, 6678, 16608])
    232
    >>> ignore_cents_and_small_amount([120, 746, 3224, 15])
    0
    >>> ignore_cents_and_small_amount([])
    0
    >>> ignore_cents_and_small_amount([12345, 50000, 4999])
    623
    """
    minimun_amount = 50 
    hundred_divisor = 100
    total = 0 
    for i in lst:
        if i > minimun_amount * hundred_divisor:
            total += i // hundred_divisor        
    return total


# Problem 2.4
def keep_dollars_only(lst):
    """
    Returns a list of dollar amount, or 'keep in vault' for other currencies

    >>> keep_dollars_only([(150, "dollars"), (80, "euros"), (120, "euros")])
    [150, 'skip', 'skip']
    >>> keep_dollars_only([(133, "euros"), (72, "rubles"), (120, "renminbi")])
    ['skip', 'skip', 'skip']
    >>> keep_dollars_only([(19, "dollars"), (275, "dollars"), (100, "dollars")])
    [19, 275, 100]
    """
    output = []
    for i in lst: 
        if i[1] == 'dollars':
            output.append(i[0])
        else: 
            output.append('skip')
        
    return output


# Problem 3
def combine_the_strings(names):
    """
    Returns a list of each name individually

    >>> combine_the_strings([("Tom", "Cruise"), ("Jon", "Voight"),("Henry",)])
    ['Tom', 'Cruise', 'Jon', 'Voight', 'Henry']
    >>> combine_the_strings([()])
    []
    >>> combine_the_strings([])
    []
    >>> combine_the_strings([("Marina", "Langlois")])
    ['Marina', 'Langlois']
    """
    output = []
    for i in names: 
        for j in i: 
            output.append(j) 
    return output


# Problem 4
def selected_name(names, char):
    """
    Return the first name for names with char in its last name

    >>> selected_name(['Marina Langlois', 'James Bond', 'Austin Madden'], 'E')
    ['Austin']
    >>> selected_name(['Martina Sampson', 'Jill Gordon', 'Cary Barber'], 's')
    ['Martina']
    >>> selected_name(['Dana Donaldson', 'Selma Owen'], 'Z')
    []
    """
    output = []
    for i in names:
        if char.lower() in i.split(" ")[-1]:
            output.append(i.split(" ")[0]) 
    return output


# Problem 5
def pay_reaction(proposed_salaries):
    """
    >>> pay_reaction([2200, 1400, 55, 1991])
    ['Will take it', 'Thinking', 'Not enough', 'Thinking']
    >>> pay_reaction([])
    []
    >>> pay_reaction([0.01, 100000])
    ['Not enough', 'Will take it']
    """
    output =[]
    for i in proposed_salaries: 
        if i <= 1000: 
            output.append('Not enough')
        elif i <= 2000: 
            output.append("Thinking")
        else:
            output.append("Will take it")      
    return output


# Question 6.1
def months_to_years(ages):
    """
    Converts each age in months from the input to the whole numbers of years

    >>> ages = [[110, 154, 345], [4, 61]]
    >>> months_to_years(ages)
    [[9, 12, 28], [0, 5]]
    >>> ages = [[], []]
    >>> months_to_years(ages)
    [[], []]
    >>> ages = [[200], [615, 0]]
    >>> months_to_years(ages)
    [[16], [51, 0]]
    """
    
    outer_list = []
    months_in_year = 12
    for i in ages:
        inner_list = []
        for j in i: 
            if j // months_in_year > 0: 
                inner_list.append(j // months_in_year)
            else: 
                inner_list.append(0)
        outer_list.append(inner_list)
    return outer_list


# Question 6.2
def harder_convert(ages):
    """
    Converts each age in months from the input to the whole numbers of years
    Replace with 0 if an age is negative

    >>> ages = [[119, 14, -34], [5, -177, -232, 362]]
    >>> harder_convert(ages)
    [[9, 1, 0], [0, 0, 0, 30]]
    >>> ages = [[], []]
    >>> harder_convert(ages)
    [[], []]
    >>> ages = [[132], [-65, 0]]
    >>> harder_convert(ages)
    [[11], [0, 0]]
    """
    outer_list = []
    months_in_year = 12
    for i in ages:
        inner_list = []
        for j in i: 
            if j // months_in_year > 0: 
                inner_list.append(j // months_in_year)
            else: 
                inner_list.append(0)
        outer_list.append(inner_list)
    return outer_list
    


# Question 6.3
def older_than_30(ages):
    """
    Counts the number of people at least as old as 30 years

    >>> ages = [[120, -154, 245], [145, -360, -615, 306]]
    >>> older_than_30(ages)
    0
    >>> ages = [[8848], [779, 0]]
    >>> older_than_30(ages)
    2
    >>> ages = [[80, -854, 900], [45, 360, 15]]
    >>> older_than_30(ages)
    2
    """
    count = 0 
    months_in_year = 12
    for i in ages:
        for j in i: 
            if j // months_in_year >= 30: 
                count += 1 
                
    return count


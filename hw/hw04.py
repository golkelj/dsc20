"""
DSC 20 Winter 2025 Homework 04
Name: Jaden Goelkel
PID: A18247795
Source: The Slides
"""

# Question 1
def place_of_birth(file_in):
    """
    From a text file, extracts the city name and the person and \
    creates a dictionary with the city name (different spelling \
    indicates a different city) as the keys and a list of the pe\
    ople from the city. 

    >>> place_of_birth('files/info_1.txt')
    {'Chicago': ['Rob'], 'New York': ['Ella'], 'New York.': ['Mary']}
    >>> place_of_birth('files/info_2.txt')
    {'Chicago': ['Rob'], 'London': ['Ezra'], 'Paris': \
['Mary'], 'paris': ['Ron', 'Harry']}
    >>> place_of_birth('files/header.txt')
    {}

    # Add at least 3 doctests below here #
    #1
    >>> place_of_birth('files/info_3.txt')
    {'San Diego': ['Sue'], 'London': ['Ben']}
    
    #2 
    >>> place_of_birth('files/info_4.txt')
    {'Paris': ['Kate']}
    
    #3 
    >>> place_of_birth('files/info_5.txt')
    {'Texas': ['Jaden']}
    
    """
    with open(file_in, "r") as reader:
        lines = reader.readlines()
    if len(lines) <= 1:
        return {}
    location = {}
    for line in lines[1:]:
        # I watched a youtube that told me that _ is a ignore value
        name, city, _ = [item.strip() for item in line.split(',')]
        if city not in location:
            location[city] = []
        location[city].append(name)
    return location

# Question 2
def age_groups(file_in, file_out):
    """
    Extracts data from a text file to then output each name and a -1 if the \
    person is younger than 35, 0 if the person is 35, or 1 is the person is \
    older than 35. This is then put in a new file with the headerline       \
    "name,older than 35" 

    >>> age_groups('files/info_1.txt', 'files/age_1_out.txt')
    >>> with open('files/age_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ella,1
    Mary,-1
    
    >>> age_groups('files/info_2.txt', 'files/age_2_out.txt')
    >>> with open('files/age_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ezra,1
    Mary,1
    Ron,0
    Harry,0

    >>> age_groups('files/header.txt', 'files/empty_out.txt')
    >>> with open('files/empty_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35

    # Add at least 3 doctests below here #
    #1 
    >>> age_groups('files/info_3.txt', 'files/age_3_out.txt')
    >>> with open('files/age_3_out.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,older than 35
    Sue,-1
    Ben,1
    
    #2
    >>> age_groups('files/info_4.txt', 'files/age_4_out.txt')
    >>> with open('files/age_4_out.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,older than 35
    Kate,1
    
    #3 
    >>> age_groups('files/info_5.txt', 'files/age_5_out.txt')
    >>> with open('files/age_5_out.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,older than 35
    Jaden,-1
    """
    current_year = 2024
    threshold_age = 35
    with open(file_in, 'r') as reader:
        lines = reader.readlines()
    with open(file_out, 'w') as writer:
        writer.write("name,older than 35\n")
        if len(lines) <= 1:
            return
        for line in lines[1:]:
            # I watched a youtube that told me that _ is a ignore value
            name, _, dob = [item.strip() for item in line.split(',')]
            yob = int(dob.split('/')[-1])
            age = current_year - yob
            if age > threshold_age:
                writer.write(f"{name},1\n")
            elif age < threshold_age:
                writer.write(f"{name},-1\n")
            else:
                writer.write(f"{name},0\n")

# Question 3
def several_files(files_lst, file_out):
    """
    This takes in a list of files with a header line and then name, city, and\
    date of birth and writes the all the information from all the files \
    (only one header) into one new files. If there is no contentin the files \
    then it will return just the header. If there is any additional whitespac\
    es they will need to be removed. 
    

    >>> lst_1 = ['files/info_1.txt','files/info_3.txt', 'files/info_4.txt']
    >>> several_files(lst_1, 'files/several_1_out.txt')
    >>> with open('files/several_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Kate,Paris,Jul 13 1945

    >>> lst_2 = ['files/info_2.txt','files/header.txt']
    >>> several_files(lst_2, 'files/several_2_out.txt')
    >>> with open('files/several_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ezra,London,Apr 12 1978
    Mary,Paris,Sep 11 1975
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989


    # Add at least 3 doctests below here #
    #1 
    >>> lst_3 = ['files/header.txt','files/header.txt']
    >>> several_files(lst_3, 'files/several_3_out.txt')
    >>> with open('files/several_3_out.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,city,DOB
    
    #2
    >>> lst_4 = ['files/info_1.txt','files/info_5.txt']
    >>> several_files(lst_4, 'files/several_4_out.txt')
    >>> with open('files/several_4_out.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    Jaden,Texas,Dec 25 2005
    
    #3
    >>> lst_5 = ['files/info_4.txt']
    >>> several_files(lst_5, 'files/several_5_out.txt')
    >>> with open('files/several_5_out.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,city,DOB
    Kate,Paris,Jul 13 1945
    """
    months = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
        '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
        '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }
    with open(file_out, 'w') as writer:
        writer.write("name,city,DOB\n")
        for file_in in files_lst:
            with open(file_in, 'r') as reader:
                lines = reader.readlines()
                for line in lines[1:]:
                    name, city, dob = [item.strip() for item
                                       in line.split(',')]
                    month, day, year = dob.split('/')
                    formatted_dob = months[month]+" "+day+" "+year
                    writer.write(name+','+city+','+formatted_dob+"\n")

# Question 4
def postcards(info_list):
    """
    Creates a dictionary with the names and modified strings. 
    
    List of tuples containing name, price, age, place is given and \
    if the age is less than 75, the first three letters of the first \
    the age, the full last name, last digit of the price, and the \
    reversed place is added to the string. 
    
    No duplicate names as the inputs
    
    >>> postcards([
    ...     ('Yue Wang', 96, 18, 'Hoover Dam'),
    ...     ('Cleo Patra', 10, 32, 'Bellagios')
    ... ])
    {'Cleo Patra': 'cle32patra0soigalleb'}
    >>> postcards([])
    {}
    >>> postcards([
    ...     ('Mari Noh', 155, 18, 'tram'),
    ...     ('Gwen Am', 34, 54, 'Venetian'),
    ...     ('Freya Dog', 34, 1, 'The Strip')
    ... ])
    {'Gwen Am': 'gwe54am4naitenev', 'Freya Dog': 'fre1dog4pirts eht'}

    # Add at least 3 doctests below here #
    >>> postcards([
    ...     ('Jaden Goelkel', 45, 22, 'Houston'),
    ...     ('Jaden Lee', 80, 50, 'Dallas')
    ... ])
    {'Jaden Goelkel': 'jad22goelkel5notsuoh'}

    >>> postcards([
    ...     ('Jaden Goelkel', 12, 30, 'Austin'),
    ...     ('Jaden Lee', 20, 19, 'San Antonio')
    ... ])
    {'Jaden Goelkel': 'jad30goelkel2nitsua', 'Jaden Lee': 'jad19lee0oinotna \
nas'}

    >>> postcards([
    ...     ('Jaden Goelkel', 74, 40, 'Fort Worth'),
    ...     ('Jaden Lee', 10, 25, 'El Paso')
    ... ])
    {'Jaden Goelkel': 'jad40goelkel4htrow trof', 'Jaden Lee': 'jad25lee0osap \
le'}
    """
    first_three = 3
    price_limit = 75
    age_index = 2
    fitler_info_list  = list(filter(lambda x: x[1] < price_limit, info_list))
    postcard_phrase = list(map(
        lambda x: ''.join([
        x[0][:first_three].lower(),
        str(x[age_index]),
        x[0].split(" ")[-1].lower(),
        str(x[1])[-1],
        x[first_three][::-1].lower()
        ]),
        fitler_info_list
    ))
    postcard_name = list(map(lambda y: y[0], fitler_info_list))
    return dict(tuple(zip(postcard_name, postcard_phrase)))

# Question 5
def win_or_lose(lst, operations):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> lst = [1, 12, 123, 1234, 12345, 123456]
    >>> operations_1 = [('advance', 5), ('lost', 3), ('tie', 4)]
    >>> win_or_lose(lst, operations_1)
    [14, 125, 1236, 12347, 123458]
    >>> operations_2 = [('lost', 200), ('eliminate', 'Team ')]
    >>> win_or_lose(lst, operations_2)
    ['Team lost', 'Team lost', 'Team lost', 'Team won', 'Team won', 'Team won']

    # Add at least 3 doctests below here #
    #1
    >>> lst = [1,2,3,4,5,]
    >>> operations_3 = [('advance', 5)]
    >>> win_or_lose(lst, operations_3)
    [6, 7, 8, 9, 10]
    
    #2
    >>> lst = [1,2,3,4]
    >>> operations = [('')]
    >>> win_or_lose(lst, operations)
    Traceback (most recent call last):
    ...
    AssertionError
    
    #3
    >>> lst = [1,py2,3,4,5]
    >>> operations_5 = [('tie', 5)]
    >>> win_or_lose(lst, operations_5)
    [5]
    
    """
    assert isinstance(lst, list)
    assert len(lst) > 0
    assert all([isinstance(i, int) for i in lst])
    assert isinstance(operations, list)
    assert all([isinstance(i, tuple) for i in operations])
    assert all([i[0] in ["advance",'lost','tie','eliminate','win'] for i in operations])
    commands = {
            'advance': lambda lst, amount: list(map(lambda x: x + amount,
                                                    lst)),
            'lost': lambda lst, amount: list(map(lambda x: x - amount,
                                                 lst)),
            'tie': lambda lst, threshold: list(filter(lambda x: x >= 
                                                      threshold, lst)),
            'eliminate':  lambda lst, symbol: list(map(lambda x: symbol + 
                                                       "won" if x > 0 
                                                       else symbol +
                                                       "lost", lst)),
            'win': lambda lst, message: message + str(sum(lst))
    }
    results = lst
    for x in operations:
        results = commands[x[0]](results, x[1])
    return results

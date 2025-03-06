"""
DSC 20 Winter 2025 Homework 08
Name: Jaden Goelkel
PID: A182477595
Source: Lecture and Readings
"""

def q1_doctests():
    """
    Doctests for Question 1.
    
    >>> broom_1 = FlyingBroom()
    >>> broom_2 = NormalBroom()
    >>> broom_3 = CursedBroom()
    >>> broom_2.boost(20)
    True
    >>> broom_1.duel(broom_2)
    False
    >>> broom_2.high_score()
    9100
    >>> broom_2.duel(broom_3)
    False
    >>> broom_2.speed
    30
    >>> broom_3.high_score()
    25750
    >>> broom_4 = CursedBroom()
    >>> broom_3.duel(broom_4)
    True
    >>> broom_4.size
    7
    >>> broom_4.speed
    20
    >>> broom_3.size
    8
    >>> broom_4.boost(40)
    True
    >>> broom_4.lives
    6
    >>> broom_4.duel(broom_2)
    True
    >>> broom_4.high_score()
    24650
    >>> broom_4.size
    8
    >>> broom_2.speed
    50

    # ADD DOCTESTS HERE #
    >>> fly_1 = FlyingBroom()
    >>> fly_2 = FlyingBroom()
    >>> fly_3 = FlyingBroom()
    >>> fly_1.boost(10)
    True
    >>> fly_1.speed
    72
    >>> fly_1.lives
    3
    >>> fly_2.boost(30)
    True
    >>> fly_2.speed
    82
    >>> fly_2.lives
    3
    >>> fly_3.boost(50)
    True
    >>> fly_3.speed
    100
    >>> fly_3.lives
    4
    
    >>> normal_1 = NormalBroom()
    >>> normal_2 = NormalBroom()
    >>> normal_3 = NormalBroom()
    >>> normal_1.boost(20)
    True
    >>> normal_1.speed
    76
    >>> normal_1.lives
    3
    >>> normal_1.duel(fly_1)
    False
    >>> normal_1.speed
    76
    >>> normal_1.lives
    3
    >>> normal_1.high_score()
    9100
    >>> normal_2.boost(10)
    True
    >>> normal_2.speed
    72
    >>> normal_2.lives
    3
    >>> normal_3.boost(40)
    True
    >>> normal_3.speed
    90
    >>> normal_3.lives
    3
    
    >>> cursed_1 = CursedBroom()
    >>> cursed_2 = CursedBroom()
    >>> cursed_3 = CursedBroom()
    >>> cursed_1.boost(20)
    True
    >>> cursed_1.duel(normal_1)
    True
    >>> cursed_1.speed
    152
    >>> cursed_1.size
    7
    >>> cursed_1.high_score()
    32150
    >>> cursed_2.boost(30)
    True
    >>> cursed_2.speed
    107
    >>> cursed_2.lives
    5
    >>> cursed_3.boost(40)
    True
    >>> cursed_3.speed
    114
    >>> cursed_3.lives
    5
    """
    return

class FlyingBroom:
    """
    Implementation of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of FlyingBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): current speed of broom, default is 50
        - size (positive int): physical size of broom, default is 5
        - magic_power (non-negative int): number of magic boosts remaining
          for this broom, default is 3
        - lives (non-negative int): number of lives a wizard has while
          flying this broom, default is 3
        """
        self.speed = 50
        self.size = 5
        self.magic_power = 3
        self.lives = 3
        pass

    def boost(self, charm_power):
        """
        Boosts the speed of the broom by using a magical
        charm. Speed boost is calculated using the formula
        specified in the write-up. If boost is successfully
        applied (enough magic power to perform boost), return True.
        Otherwise (no remaining magic power to perform boost), return False.
        
        Parameters:
        - charm_power (int): used to calcualte speed boost formula.
          Applied as long the broom still has some magic power
          remaining.
        """
        if self.magic_power < 1:
            return False
        d_num = 2
        h_num = 0.5
        new_speed = int(((self.speed + charm_power) ** d_num +
                          (self.speed - charm_power) ** d_num ) ** h_num)
        if new_speed >= d_num * self.speed:
            self.lives += 1
        self.magic_power -= 1
        self.speed = new_speed
        return True
        
    def set_speed(self, new_speed):
        """
        Setter method that assigns given speed value to 
        speed attribute.
        
        Parameters:
        - new_speed (int): new speed value
        """
        self.speed = new_speed
        pass

    def set_lives(self, gains = True):
        """
        Setter method that increments lives attribute 
        by 1 if gains is True, otherwise decrement by 1.
        
        Parameters:
        - gains (bool): decides whether to increment/decrement
          lives attribute by 1.
        """
        if gains:
            self.lives += 1
        else: 
            self.lives -= 1 

    def set_size(self, new_size):
        """
        Setter method that assigns given size value
        (non-negative) to size attribute.
        
        Parameters:
        - new_size (non-negative int): new size value
        """
        self.size = new_size

    def duel(self, other_broom):
        """
        Determines if a duel can occur between
        current broom and other_broom. If so,
        the following happens as specified in
        the write-up. Return True if current
        broom successfully performs duel, otherwise
        False.
        
        Parameters:
        - other_broom (object): Broom object
        """
        speed_change = 50
        if self.size > other_broom.size:
            other_broom.speed -= speed_change
            self.speed += speed_change
            if other_broom.speed <= 0:
                other_broom.lives -= 1
                other_broom.speed = speed_change
                self.size += 1
            return True
        if other_broom.size>self.size:
            self.speed -= speed_change
            other_broom.speed += speed_change
            if self.speed <= 0:
                self.lives -= 1
                self.speed = speed_change
                other_broom.size += 1
        return False

    def high_score(self):
        """
        Formula for high score and returns it.
        """
        mult_100 = 100
        mult_500 = 500
        return self.speed * mult_100 + self.lives * mult_500 

class NormalBroom(FlyingBroom):
    """
    Implementation of NormalBroom. Subclass of FlyingBroom.
    """
    def duel(self, other_broom):
        """
        Duel method for NormalBroom.
        - If other_broom is an instance of CursedBroom,
          current NormalBroom loses one life, and its speed 
          resets to 30.
        - CursedBroom object gains a size, and its speed
          increases by 50.
        - Attack is thus considered unsuccessful, function
          returns False.
        - If other_broom is not a CursedBroom object, duel
          method is the same as in the parent class.
        
        Parameters:
        - other_broom (object): Broom object
        """
        reset = 30
        change = 50
        if isinstance(other_broom, CursedBroom):
            self.lives -= 1
            self.speed = reset
            other_broom.size += 1
            other_broom.speed += change
            return False
        return super().duel(other_broom)

class CursedBroom(FlyingBroom):
    """
    Implementation of CursedBroom. Subclass of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of CursedBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): default is 70
        - size (positive int): default is 7
        - magic_power (non-negative int): default is 5
        - lives (non-negative int): default is 5
        """
        self.speed = 70
        self.size = 7
        self.magic_power = 5
        self.lives = 5

    def high_score(self):
        """
        Formula for a CursedBroom high score and returns it.
        """
        mult_200 = 200
        mult_300 = 300
        add_250 = 250
        return (self.speed * mult_200) + (self.lives * mult_300) + add_250
        
# Question 2
# Q2, Part 1
def fix_1(lst1, lst2):
    """
    This function takes in two lists and trys to divide the items of the first\
     list by the items in the second list and then append to a new list. 

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    
    # NO DOCTESTS NEEDED #
    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div) # add try-catch block
            except ZeroDivisionError:
                continue
    return out

# Q2, Part 2
def fix_2(*filepaths):
    """
    Trys to open filepaths and prints whether it was successful or not
    
    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found
    >>> fix_2('docs.txt')
    docs.txt not found
    
    # NO DOCTESTS NEEDED #
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r") # add try-catch block
            print(f'{filepath} opened')
            cur_file.close()
        except FileNotFoundError:
            print(f'{filepath} not found')

# Q2, Part 3
def fix_3(lst):
    """
    Goes through a list add the current item at index to the next item at the \
    next index and then append the value to a list or prints the error type
    
    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []
    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]
    >>> fix_3([])
    []
    
    # NO DOCTESTS NEEDED #
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1]) # add try-catch block
        except (TypeError, IndexError) as a:
            print(type(a))
    return sum_of_pairs


# Question 3
def check_inputs(input1, input2):
    """
    Checks the correctness of input1 and input2 and prints "input validated" 
    or returns the exception. 
    -must be a list, with all values being numeriacl, input needs to be in \
    input 1

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'
    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    
    # Add at least 3 doctests below here #
    >>> check_inputs(100, 100)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs([1, 2, 'jaden'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    >>> check_inputs([45, 2.0, 3.0], 'jaden')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    
    """
    if not isinstance(input1, list):
        raise TypeError('input1 is not the correct type')
    for idx, x in enumerate(input1):
        if not isinstance(x, (int, float)):
            raise TypeError(f'The element at index {idx} is not numeric')
    if not isinstance(input2, (int, float)):
        raise TypeError('input2 is not the correct type')
    if input2 not in input1:
        raise TypeError('input2 not in input1')
    return 'Input validated'

# Question 4
def load_file(filepath):
    """
    Takes a filepath and returns the number of words in the file, there is \
    tests that needs to pass and if none of the test pass, the exception will \
    return
    
    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    >>> load_file('files/ten_words.txt')
    10
    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty
    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist
    
    # Add at least 3 doctests below here #
    >>> load_file(2)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    >>> load_file('files/poopoo.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/poopoo.txt does not exist
    >>> load_file('files/jadne.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/jadne.txt does not exist
    
    """
    if not isinstance(filepath, str):
        raise TypeError('filepath is not a string')
    try:
        with open(filepath, 'r') as f:
            content=f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'{filepath} does not exist')
    in_content=content.split()
    if not in_content:
        raise ValueError('File is empty')
    return len(in_content)
    
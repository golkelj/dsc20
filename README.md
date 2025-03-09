# dsc20
winter 25 


## HOF 
function()() 
- First () is the outer function and the second () 
is the inner function
- does stuff from left to right

- if you do not add the parameters to a function you can accomplish it by call () outside

- if the inner function is defined within the outer function you must called it with 
function()() 

- if the function is defined on the outside you do not need to call it 

``` range() ```
- range(start, stop, step)
    - start: inclusive
    - stop: exclusive
    - step: jump

``` print() ```
- print: returns none
- the inner statement will excute first
    - so if you print(print(__)) it will print the __ then it will return none

# dsc20 notes

## Errors 
- Syntax Error 
- semantic Error 
- Exceptions  
    - NameError 
    - IndexError 
    - KeyError 
    - ValueError = correct type but doesnt fit parameter 
    - TypeError = wrong type
    - ImportError 
    - AttributionError
    - ZeroDivisionError   


### Slicing 
[start:stop:step]

## Data types 

### String 

``` string.find("", start, stop ) ```

- returns the index of the given letter or -1 if it is not found 

``` in ```

- This boolen operator finds if a string is in a string   

### List
- Slicable
- Mutable 

```list.append() ``` 
- Adds single item to the list (can be different types)
- modifies and returns none

``` .list() ```
- Turns items into a list
- Index values must be integers 


```list.extend()```

- Adds iterable item to the list 

### Tuple 
- Slicable  
- Immutable


#### Tuple assigment 

``` a, b = b, a ```

- numbers on both sides need to be the same lenght  
- The right side of expression is unpacked before any of the assignment

- To specify a tuple with only one element in an assignment statement, simply follow the element with a comma

### String
- Slicable
- Immutable

### Dictonaries 
- Allows you to associate _values_ with _keys_  
- Ordered collections of _key_value_ pairs  

``` dict = {'key': 'value', ... , 'key': value} ```

- *keys* can be any immutable data types (tuples, strings, boolean, numerics (int, float, complex) )  
- *values* can be any data types  

``` dict.get(key) ```

- Gives value at the key 

``` del dict[key] ```

- Deletes the key value pairs

``` dict.keys() ```

- returns the keys (Note it does not return a list; If you want to use the values into a list by casting)

``` dict[] = __ ```   
- Adds a key value pair to a dictionary

- The order on the computer might not be the same** 

``` dict[key] ```
- returns the value at the key or it returns KeyError

``` in ``` works for dicts and will return bool is the key is present 

#### - Can be used as a counter 

immutable - the value cannot be changed 
    - string 
    - int
    - tuple 
    - bool
    - float 

mutable 
    - list 
    - dict

all objects that are related to a object can be mutated
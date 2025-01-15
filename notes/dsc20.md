# dsc20 notes
### Slicing 
[start:stop:step]

## Data types  
### List
- Slicable
- Mutable 

```list.append() ``` 
- Adds single item to the list (can be different types)

``` .list() ```
- Turns items into a list 


```list.extend()```

- Adds iterable item to the list 

### Tuple 
- Slicable  
- Immutable

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




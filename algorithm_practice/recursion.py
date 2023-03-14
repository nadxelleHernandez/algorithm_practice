def factorial(num):
    if num < 0:
        raise ValueError("Num must be greater than zero")
    if num == 0:
        return 1
    else:
       return num * factorial(num-1)

def reverse(text):
    if not text:
        return ""

    str_len= len(text)
    if  str_len == 1:
        return text
    else:
        return text[-1] + reverse(text[:-1])

def bunny(num):
    if not num:
        return 0

    if num == 1:
        return 2
    
    return 2 + bunny(num-1)

def is_nested_parens(parentesis):
    if not parentesis:
        return True

    str_len = len(parentesis)

    if parentesis[0]=='('and parentesis[-1]!=')':
        return False
    if parentesis[0]==')':
        return False

    return is_nested_parens(parentesis[1:-1])

def search(array,query):
    if not array:
        return False

    if array[0] == query:
        return True
    else:
        return search(array[1:],query)

def is_palindrome(text):
    if not text:
        return True

    text_len = len(text)
    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])
    
def digit_match(number1, number2):
    if number1 == number2:
        return 1

    if number1 == 0 or number2 == 0:
        return 0
    
    next_number1 = number1 // 10
    next_number2 = number2 // 10
    
    if (number1 % 10) == (number2 % 10):
        return 1 + digit_match(next_number1,next_number2)
    
    if next_number1 == 0 and next_number2 == 0:
        return 0
    
    return digit_match(next_number1,next_number2)


def min_max(arr):
    '''
    INPUT: 1-dimensional array with integers which can be either positive or negative
    OUTPUT: Tuple where the first element is the minimum element in the array and the second element is the maximum element in the array.

    Example input:
    [7, 1, 8, 5, 10, 4, 2, 6]

    Example output:
    (1, 10)
  '''
    
    if not arr:
        return None
    
    arr_len = len(arr)
    min = 0
    max = 0
    
    if arr_len == 1:
        return arr[0],arr[0]

    if arr_len == 2:
        if arr[0] < arr[1]:
           min = arr[0]
           max = arr[1]
        else:
           min = arr[1]
           max = arr[0]
        return min,max
    
    mid = arr_len//2
    min_max_right = min_max(arr[:mid]) 
    min_max_left = min_max(arr[mid:])

    if min_max_right[0] < min_max_left[0]:
        min = min_max_right[0]
    else:
        min = min_max_left[0]

    if min_max_right[1] > min_max_left[1]:
        max = min_max_right[1]
    else:
        max = min_max_left[1]

    return min,max
 
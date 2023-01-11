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


    

    
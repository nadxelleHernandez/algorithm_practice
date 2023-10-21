def camelcase(s)-> int:
    if not s:
        return 0
    
    words = 1
    for char in s:
        if char.isupper():
            words += 1

    return words

def get_symmetric_pairs(pairs_list):
    if not pairs_list:
        return []

    pairs_hash = dict() 
    for elem in pairs_list:
        pairs_hash[elem[0]] = elem[1]
        
    symmetric = list()
    for elem in pairs_list:
        first = pairs_hash.get(elem[1])
        if first is None: #there is no pair with that combination
            continue
            
        if first == elem[0]: #we found a pair
            symmetric.append(elem)
            pairs_hash.pop(elem[0])
            pairs_hash.pop(elem[1])
            
    return symmetric

def get_intersection(list1, list2):
    if not list1 or not list2:
        return []

    helper = dict()
    for elem in list1:
        if elem not in helper:
            helper[elem] = 1
        else:
            helper[elem] += 1

    intersection = list()
    for elem in list2:
        if elem in helper and helper[elem] > 0:
            intersection.append(elem)
            helper[elem] += -1

    return intersection
            
def is_permutation(str1, str2):
    if not str1 or not str2:
        return False

    helper = dict()
    for char in str1:
        if char not in helper:
            helper[char] = 1
        else:
            helper[char] += 1
    
    for char in str2:
        if char not in helper or helper[char] <= 0:
            return False
        
        helper[char] += -1

    for value in helper.values():
        if value != 0:
            return False

    return True

def even(num: int):
    return num % 2 == 0

def is_palindrome_permutation(word):
    if not word:
        return False

    num_chars = dict()

    for char in word:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1

    num_not_even = 0
    word_len = len(word)
    for count in num_chars.values():
        even_count = even(count)
        if not even(word_len) and not even_count:
            num_not_even += 1
            if num_not_even >= 2:
                return False

        elif not even_count:
            return False

    return True

def server_failures(logs: [str]):
    '''
    Given n number of servers, tell how many time had they needed to be restarted. A server is restarted when it fails three times. This failures can be located on the 
    logs array as: s1 failed for server 1, s2 failed for server 2 etc.
    '''

    failure_dict = {}
    for s in logs:
        if "failed" in s:
            if s in failure_dict:
                failure_dict[s] += 1
            else:
                failure_dict[s] = 1

    times_failed = 0
    for fail in failure_dict.values():
        if fail >= 3:
            times_failed += fail // 3

    return times_failed


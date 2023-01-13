def insert_sort(lst):
    if not lst:
        return []

    last_ordered_i = 0
    lst_len = len(lst)
    for index in range(lst_len):
        elem = lst[index]
        if index == 0:
            continue
        if elem < lst[last_ordered_i]:
            lst[index] = lst[last_ordered_i]
            i = last_ordered_i
            finding = True
            while finding:
                finding = lst[i] > elem
                if finding and i >= 0:
                    lst[i+1] = lst[i]
                elif finding and i < 0:
                    lst[0] = elem
                    finding = False
                else:
                    lst[i+1] = elem
                i -= 1
        last_ordered_i += 1    

    return lst


def sort_by_length(string):
    if not string or type(string) is not str:
        return []

    words = string.split()

    last_ordered_i = 0
    words_len = len(words)
    for index in range(words_len):
        word = words[index]
        if index == 0:
            continue
        if len(word) < len(words[last_ordered_i]):
            words[index] = words[last_ordered_i]
            i = last_ordered_i
            finding = True
            while finding:
                finding = len(words[i]) > len(word)
                if finding and i >= 0:
                    words[i+1] = words[i]
                elif finding and i < 0:
                    words[0] = word
                    finding = False
                else:
                    words[i+1] = word
                i -= 1
        last_ordered_i += 1 
    return words
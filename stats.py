def get_number_of_words(text):
    return len(str.split(text, ' '))

def get_letter_occurance(text):
    dict = {}
    for letter in text:
        letter = str.lower(letter)
        if letter in dict:
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_letter_count_by_size(dict_with_count):
    sorted_list = []
    for k in dict_with_count:
        if k.isalpha():
            sorted_list.append({"letter":k, "num": dict_with_count[k]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_sorted_letter_count(text):
    dict = get_letter_occurance(text)
    return sort_letter_count_by_size(dict)

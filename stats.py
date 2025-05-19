def get_num_words(string):
    word_list = string.split()
    num_words = len(word_list)
    return num_words


def get_chars_dict(string):
    chars_dict = {}
    for c in string:
        c = c.lower()
        if c in chars_dict:
            chars_dict[c] += 1
        else:
            chars_dict[c] = 1
    return chars_dict


def get_sorted_list_of_dicts(count_dict):
    list = []
    for key, val in count_dict.items():
        list.append({"char": key, "num": val})
    list.sort(reverse=True, key=lambda x: x["num"])
    return list
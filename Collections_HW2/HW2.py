import random as rn

def generate_random_dict():
    # generate random number of keys (out of scope in HW)
    random_number_of_keys = rn.randint(1, 10)
    # generate keys with help of ascii (only lowercase letters)
    keys = [chr(rn.randint(97, 122)) for char in range(random_number_of_keys)]
    # return dict, where for each generated key we also generate number from 0 to 100
    return {key: rn.randint(0, 100) for key in keys}
def generate_list_of_dict():
    # generate random number of dicts
    dict_number = rn.randint(2, 10)
    # return generated random dicts in a list
    return [generate_random_dict() for dict in range(dict_number)]

def dict_flattening(list_of_dicts):
    # list rather for performance. E.g. if we checked some value in one dict,
    # there is no sense to return to it in further dicts
    checked_items = []
    # container for final values
    flatten_dict = {}
    # traverse through all dicts
    for i in range(len(list_of_dicts)):
        # traverse through all values in each dict
        for key, value in list_of_dicts[i].items():
            # if we checked this value, in previous dicts, just skip
            if key in checked_items:
                continue
            # variables to understand the maximum value and for renaming (if needed) the key
            max_key = key
            max_value = value
            # try to find key in other dicts
            for j in range(len(list_of_dicts)):
                # key - value from other dicts
                dict = list_of_dicts[j]
                value_from_other_dict = dict.get(key)
                if i == j:
                    continue
                # if there are duplicates in keys, but the first occurence is max, just rename key
                elif value_from_other_dict is not None and value_from_other_dict <= max_value:
                    max_key = max_key + '_' + str(i + 1)
                # if there are duplicates and the first value isn't max, rename key and reassign max value
                elif value_from_other_dict is not None and value_from_other_dict > max_value:
                    max_value = value_from_other_dict
                    max_key = max_key + '_' + str(j + 1)
            checked_items.append(key)
            # add maximum value and respective key to container
            flatten_dict[max_key] = max_value

    return flatten_dict

# generate our list of dictionaries
rand_dict = generate_list_of_dict()
# print(rand_dict)
# flatten the dict and print it
print(dict_flattening(rand_dict))
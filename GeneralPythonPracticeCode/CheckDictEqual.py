def compare_dicts(dict1, dict2):
    # Check if both dictionaries are equal
    if dict1 == dict2:
        return "The dictionaries are equal."

    # Check for keys that are in dict1 but not in dict2
    print("====================================================================================")
    missing_in_dict2 = dict1.keys() - dict2.keys()
    if missing_in_dict2:
        print(f"Keys in dict1 but not in dict2: {missing_in_dict2}")

    # Check for keys that are in dict2 but not in dict1
    print("====================================================================================")
    missing_in_dict1 = dict2.keys() - dict1.keys()
    if missing_in_dict1:
        print(f"Keys in dict2 but not in dict1: {missing_in_dict1}")

    # Check for differing values for common keys
    print("====================================================================================")
    differing_values = {key: (dict1[key], dict2[key]) for key in dict1.keys() & dict2.keys() if dict1[key] != dict2[key]}
    if differing_values:
        print("Differing values for common keys:")
        for key, values in differing_values.items():
            print(f"Key '{key}': dict1 has {values[0]}, dict2 has {values[1]}")

    return "The dictionaries are not equal."

# Example usage
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'a': 1, 'b': 3, 'd': 4}

result = compare_dicts(dict_a, dict_b)
print(result)

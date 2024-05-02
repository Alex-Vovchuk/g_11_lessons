another_set = {1, 6, 11, 16, 20}
example_list = 26
another_dict = {
    example_list:  25,
    'string': [1, 2, "string"],
    12: {
        "another_key": [12, 15],
        "another_value": "string"
    }
}


my_answers = []
for key in another_dict:
    my_answers.append(key)
print(my_answers)





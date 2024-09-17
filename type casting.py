def main():
    # Convert float to int
    float_number = 10.7
    integer_number = int(float_number)
    print(f"Float to int: {float_number} -> {integer_number}")

    # Convert int to float
    integer_number = 5
    float_number = float(integer_number)
    print(f"Int to float: {integer_number} -> {float_number}")

    # Convert int to str
    integer_number = 42
    string_number = str(integer_number)
    print(f"Int to str: {integer_number} -> '{string_number}'")

    # Convert tuple to list
    tuple_data = (1, 2, 3)
    list_data = list(tuple_data)
    print(f"Tuple to list: {tuple_data} -> {list_data}")

    # Convert list to tuple
    list_data = [4, 5, 6]
    tuple_data = tuple(list_data)
    print(f"List to tuple: {list_data} -> {tuple_data}")

    # Convert list to set
    list_data = [1, 2, 2, 3, 4]
    set_data = set(list_data)
    print(f"List to set: {list_data} -> {set_data}")

    # Convert list of tuples to dict
    tuple_list = [('x', 10), ('y', 20), ('z', 30)]
    dict_data = dict(tuple_list)
    print(f"List of tuples to dict: {tuple_list} -> {dict_data}")

if __name__ == "__main__":
    main()
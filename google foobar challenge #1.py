def solution(data, n):
    # Get a list of all the unique variables in data
    data_set = list(set(data))
    new_data = []
    amount_of_var = []

    # Since we'll be popping the list we need to ensure the original data's integrity
    new_data.extend(data)

    # Make the entire meat of the function iterates repeats for all the unique ints
    for x in range(len(data_set)):

        # Repeats for all ints in original data list
        for i in data:

            # Selects the int we're looking for
            variable_want_to_find = data_set[x]

            # Go through the list, find each instance of the variable and then pop() it. make a list of where we
            # popped it from, so we can apply that list to a remove() function in actual data if len(amount_of_var) < n
            for t in range(len(new_data)):
                try:
                    pop_value = new_data.index(variable_want_to_find)
                    amount_of_var.append(new_data.pop(pop_value))
                except:
                    pass

            # Check the amount of ints found against the n value and use remove to take them off of the original data
            if len(amount_of_var) <= n:
                del amount_of_var[:]        # The .clear() function doesn't work in the python version they test in
            else:
                try:
                    for l in range(len(amount_of_var)):
                        data.remove(variable_want_to_find)
                except:
                    del amount_of_var[:]
    return data

def binaryInsertionSort(list):
    """
    Takes a list of numbers, and returns them in ascending order.
    Uses a binary insertion sort method, to speed things up

    :param list: The list to sort
    :returns: The sorted list
    """
    sorted_list = []

    for item in list:
        # Handle Empty List
        if len(sorted_list) == 0:
            sorted_list.append(item)
            continue
        # Handle list with 1 item
        if len(sorted_list) == 1:
            if item > sorted_list[0]:
                sorted_list.append(item)
            else:
                sorted_list.insert(0, item)
            continue
        # Handle it being lower than the first item in the list (it cant)
        if item < sorted_list[0]: # Safe to use sorted_list[0] as it is caught by the first if statement.
            sorted_list.insert(0, item)
        lower_bound = 0
        upper_bound = len(sorted_list) - 2
        midpoint = 0
        added = False

        while upper_bound >= lower_bound:
            midpoint = (lower_bound + upper_bound) // 2
            # Checks the value at and above the midpoint. If the value being added is between the upper and lower value, add it to the list in that spot (midpoint + 1). Allows them being the same
            if sorted_list[midpoint] <= item <= sorted_list[midpoint + 1]:
                sorted_list.insert(midpoint + 1, item)
                added = True
                break
            # If the upper value is less than the item, set lower bound to midpoint + 1
            elif sorted_list[midpoint + 1] <= item:
                lower_bound = midpoint + 1
            # If the lower value is more than the item, set upper bound to midpoint
            elif sorted_list[midpoint] >= item:
                upper_bound = midpoint - 1
        if not added:
            sorted_list.append(item)
    return sorted_list

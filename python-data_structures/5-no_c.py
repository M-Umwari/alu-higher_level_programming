list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = list(my_list)
        new_list[idx] = element
        return new_list



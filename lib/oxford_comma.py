def oxford_comma(items):

    for item in items:
        if len(items) > 2:
            string_list = ", ".join(items[:-1]) + ", and " + str(items[-1])
            return string_list
        elif len(items) > 1:
            string_list = " and ".join(items)
            return string_list
        else:
            return item

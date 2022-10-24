def connected_tuples(pairs):
    # for every element, we keep a reference to the list it belongs to
    lists_by_element = {}

    def make_new_list_for(x, y):
        lists_by_element[x] = lists_by_element[y] = [x, y]

    def add_element_to_list(lst, el):
        lst.append(el)
        lists_by_element[el] = lst

    def merge_lists(lst1, lst2):
        merged_list = lst1 + lst2
        for el in merged_list:
            lists_by_element[el] = merged_list

    for x, y in pairs:
        xList = lists_by_element.get(x)
        yList = lists_by_element.get(y)

        if not xList and not yList:
            make_new_list_for(x, y)

        if xList and not yList:
            add_element_to_list(xList, y)

        if yList and not xList:
            add_element_to_list(yList, x)            

        if xList and yList and xList != yList:
            merge_lists(xList, yList)

    # return the unique lists present in the dictionary
    return set(tuple(l) for l in lists_by_element.values())


cpairs =  connected_tuples(mypairs)
print(list(cpairs)[0:30])

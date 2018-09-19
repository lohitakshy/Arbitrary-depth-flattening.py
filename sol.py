def flatten(list_of_array):
     for list1 in list_of_array:
            if isinstance(list1, list):
                for ele in flatten(list1):
                    yield ele
            else:
                yield list1
y = list(flatten(x))
print(y)

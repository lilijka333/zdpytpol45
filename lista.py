def simple_list(data: list) -> list:
    simple_list = []

    for i in data:
        try:
            for j in i:
                simple_list.append(j)
        except:
            simple_list.append(i)

example = [1, [2, [3, 4]], 5, [6, 7], 8, [9, [10]]]

# print(simple_list(example))


def flat_list(lst):
    return [item for sublist in lst for item in sublist]

print(flat_list(example))
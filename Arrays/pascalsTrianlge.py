def printPascal(n: int):
    # min value of n is one
    final = [[1]]

    for i in range(1, n):
        len_new_list = len(final[-1])+1
        new_list = [1, 1]
        prev_list = final[-1]
        for j in range(2, len_new_list):
            new_list.insert(j-1, prev_list[j-2]+prev_list[j-1])
        final.append(new_list)

    return final


print(printPascal(5))

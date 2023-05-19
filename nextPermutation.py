def nextPermutation(permutation, n):
    final_list = []
    j = -1
    for i in range(n-1, -1, -1):
        if permutation[i] > permutation[i-1]:
            j = i-1
            break
    if j == -1:
        return sorted(permutation)

    final_list = permutation[:j]
    new_list = permutation[j:]
    for i in range(len(new_list)-1, -1, -1):
        if new_list[i] > permutation[j]:
            k = i
            final_list.append(new_list[k])
            del new_list[i]
            break

    final_list = final_list + sorted(new_list)
    return final_list


permutation = [1, 3, 2]
print(nextPermutation(permutation, len(permutation)))

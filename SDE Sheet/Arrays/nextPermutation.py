def nextPermutation(permutation, n):
    j = -1
    for i in range(len(permutation)-1, -1, -1):
        if permutation[i] > permutation[i-1]:
            j = i-1
            break
    if j == -1:
        permutation = permutation[::-1]

    else:
        for k in range(len(permutation)-1, j, -1):
            if permutation[k] > permutation[j]:
                permutation[k], permutation[j] = permutation[j], permutation[k]
                break
        permutation[j+1:] = permutation[j+1:][::-1]

    return permutation


print(nextPermutation([1, 2, 3], 3))

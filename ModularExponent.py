def modularExponentiation(x, n):
    ans = 1
    nn = n
    if n < 0:
        nn = -1 * n

    while (nn > 0):
        if nn % 2 == 1:
            ans = x * ans
            nn = nn - 1
        else:
            x = x * x
            nn = nn / 2

    if n < 0:
        ans = 1 / ans

    return ans


# time = log(N)
print(modularExponentiation(2, 5))

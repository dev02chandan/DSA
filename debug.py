ds = [1, 2, 3]
ans = []
ans.append(ds)
ds = [1, 2]
ans.append(ds)
print(ans)

ds = [1, 2, 3]
ans = []
ans.append(ds[:])
ds = [1, 2]
ans.append(ds[:])
print(ans)

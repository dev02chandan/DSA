def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    left = m-1
    right = 0
    nums1 = nums1[:m]

    while (left >= 0 and right < n):
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left -= 1
            right += 1
        else:
            break

    nums1.sort()
    nums2.sort()

    nums1 = nums1 + nums2
    # nums1 = nums1[n:]
    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

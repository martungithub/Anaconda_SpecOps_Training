def merge_soted_array(nums1, m, nums2, n):
    k = 0
    for i in range(m, m + n):
        nums1[i] = nums2[k]
        k += 1
    nums1.sort()
    return nums1


print(merge_soted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

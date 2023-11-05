def merge_lists(nums1, n, nums2, m):
    # Initialize pointers for nums1, nums2, and merged array
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    # Merge nums1 and nums2 from the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Copy remaining elements from nums2 to nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]


nums1 = [1, 2, 3, 0, 0, 0, 0]
m = 3
nums2 = [-4, 2, 3, 9]
n = 4

print(merge_lists(nums1, m, nums2, n))

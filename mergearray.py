def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Initialize pointers for nums1, nums2, and the merged array (from the end)
    p1 = m - 1
    p2 = n - 1
    p_merged = m + n - 1

    # Iterate while there are elements in both nums1 and nums2
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p_merged] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
        p_merged -= 1

    # If there are any remaining elements in nums2, copy them to nums1
    while p2 >= 0:
        nums1[p_merged] = nums2[p2]
        p2 -= 1
        p_merged -= 1

# Example usage:
nums1_1 = [1, 2, 3, 0, 0, 0]
m1 = 3
nums2_1 = [2, 5, 6]
n1 = 3
merge(nums1_1, m1, nums2_1, n1)
print(f"Merged array 1: {nums1_1}")  # Output: [1, 2, 2, 3, 5, 6]

nums1_2 = [1]
m2 = 1
nums2_2 = []
n2 = 0
merge(nums1_2, m2, nums2_2, n2)
print(f"Merged array 2: {nums1_2}")  # Output: [1]

nums1_3 = [0]
m3 = 0
nums2_3 = [1]
n3 = 1
merge(nums1_3, m3, nums2_3, n3)
print(f"Merged array 3: {nums1_3}")  # Output: [1]

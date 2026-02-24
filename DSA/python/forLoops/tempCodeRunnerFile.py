nums1 = [10,43,54,21,42]
nums2 = [34,65,34,83]
nums3 = nums1 + nums2
temp = 0
for i in nums3:
    temp += i
print(round(temp / len(nums3)))
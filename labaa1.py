

def is_subarray(nums1, nums2):

    len1, len2 = len(nums1), len(nums2)
    
    index2 = 0
    
    for index1 in range(len1):
        while index2 < len2 and nums1[index1] != nums2[index2]:
            index2 += 1
        
        if index2 == len2:
            return False
        
        index2 += 1
    
    return True

nums1 = [1, 2, 3, 0]
nums2 = [0, 1, 2, 3, 4, 0]
result = is_subarray(nums1, nums2)
print(result)
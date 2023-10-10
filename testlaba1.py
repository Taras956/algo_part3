import testlaba1
import unittest

class TestIsSubarray(unittest.TestCase):

    def test_subarray_present(self):
        nums1 = [1, 2, 3]
        nums2 = [0, 1, 2, 3, 4, 5]
        result = is_subarray(nums1, nums2)
        self.assertTrue(result)

    def test_subarray_not_present(self):
        nums1 = [1, 2, 3]
        nums2 = [0, 1, 2, 4, 5]
        result = is_subarray(nums1, nums2)
        self.assertFalse(result)

    def test_empty_subarray(self):
        nums1 = []
        nums2 = [0, 1, 2, 3, 4, 5]
        result = is_subarray(nums1, nums2)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
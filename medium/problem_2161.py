class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1 = []
        list2 = []
        list3 = []
        for i in range(0, len(nums)):
            if nums[i] < pivot:
                list1.append(nums[i])
            elif nums[i] == pivot:
                list2.append(nums[i])
            else:
                list3.append(nums[i])
            i += 1
        nums = list1 + list2 + list3
        return nums
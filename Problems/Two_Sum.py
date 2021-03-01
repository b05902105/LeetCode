#1. Two Sum
#Easy
class Solution(object):
	def twoSum(self, nums, target):
		dict = {}
		for i, n in enumerate(nums):
			try:
				return [dict[target - n], i]
			except:
				dict[n] = i
if __name__ == '__main__':
	solver = Solution()
	print(solver.twoSum([3, 2, 4], 6))

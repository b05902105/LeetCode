#Distribute Candies

class Solution(object):
	def distributeCandies(self, N):
		return min(len(N)//2, len(set(N)))
        
if __name__ == '__main__':
	candyType = [1,1,2,3]
	solver = Solution()
	print(solver.distributeCandies(candyType))


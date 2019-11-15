#LEETCODE:>>>

#floodFill problem:>>>
class Solution:
    def floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] == newColor: return image
        self.fill(image, newColor, image[sr][sc], sr, sc)
        return image
    
    def fill(self, im, newC, pixelValue, i, j):
        if i < 0 or j < 0 or i >= len(im) or j >= len(im[0]) or im[i][j] != pixelValue:
            return
        im[i][j] = newC
        self.fill(im, newC, pixelValue, i+1, j)
        self.fill(im, newC, pixelValue, i-1, j)
        self.fill(im, newC, pixelValue, i, j+1)
        self.fill(im, newC, pixelValue, i, j-1)

solution = Solution()

#Testing the Solution with some random cases:>>
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))  #[[2,2,2],[2,2,0],[2,0,1]]
print(solution.floodFill([[0,0,0],[0,1,1]], 1, 1, 1)) #[[0,0,0],[0,1,1]]
print(solution.floodFill([[1,0,1],[0,0,0],[1,0,1]], 1, 1, 100))  #[[1,100,1],[100,100,100],[1,100,1]]
print(solution.floodFill([[0,0,0],[1,1,1],[0,0,0]], 1, 1, 12))   #[[0,0,0],[12,12,12],[0,0,0]]
print(solution.floodFill([], 1, 1, 2))  #[]

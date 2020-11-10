'''
Inputs: 2-D array of integers, each integer representing a pixel, starting pixel row and column, and a pixel value newColor.

Perform a "flood fill" - change the starting pixel to newColor, plus any pixels connected 4-directionally to the starting pixel of the same color, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel)

Example:
image = [
  [1,1,1],
  [1,1,0],
  [1,0,1]
  ]
sr = 1, sc = 1, newColor = 2

Output: 
image = [
  [2,2,2],
  [2,2,0],
  [2,0,1]
  ]
'''

def floodFill(image, sr, sc, newColor):
  oldColor = image[sr][sc]
  if oldColor == newColor:
      return image

  def changeColor(r, c):
      image[r][c] = newColor
      checkNeighbors(r, c)

  def checkNeighbors(r, c):
      if r > 0 and image[r-1][c] == oldColor:
          changeColor(r-1, c)

      if r < len(image)-1 and image[r+1][c] == oldColor:
          changeColor(r+1, c)

      if c < len(image[0])-1 and image[r][c+1] == oldColor:
          changeColor(r, c+1)

      if c > 0 and image[r][c-1] == oldColor:
          changeColor(r, c-1)

  changeColor(sr, sc)
  return image

print(floodFill([
  [1,1,1],
  [1,1,0],
  [1,0,1]
  ], 1, 1, 2))

# => [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
"""
Exercise 3
Time complexity: O(log(n))
"""


def chessboardSpace(numberOfGrains):
    chessboardSpaces = 1
    placedGrains = 1
    
    while placedGrains < numberOfGrains:
        placedGrains *= 2
        chessboardSpaces += 1
        
    return chessboardSpaces
    
    
if __name__ == '__main__':
    nums = [16, 32, 64, 128, 256, 512, 1024]
    
    for i in nums:
        print(f'{i} grains will be placed on the {chessboardSpace(i)}th square')

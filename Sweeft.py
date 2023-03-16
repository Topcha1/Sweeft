#1
num = int(input())
dear = {}
for i in range(num):
    word = input()
    if word in dear:
        dear[word] += 1
    else:
        dear[word] = 1

print(len(dear))
for key, value in dear.items():
    print(value, end=" ")

#2

def bigger_is_greater(word):
    sitkva = list(word)
    i = len(word) - 1
    while i > 0 and sitkva[i - 1] >= sitkva[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    k = len(word) - 1
    while sitkva[k] <= sitkva[i - 1]:
        k -= 1
    sitkva[i - 1], sitkva[k] = sitkva[k], sitkva[i - 1]
    sitkva[i:] = sitkva[len(sitkva) - 1:i - 1:-1]
    return ''.join(sitkva)


n = int(input("enter the number: "))
for i in range(n):
    word = input("enter word: ")
    print(bigger_is_greater(word))


#3
import sys
import time


def bomber_man(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                grid[i][j] = 'O'
            else:
                grid[i][j] = 'B'

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'B':
                if i > 0:
                    if grid[i][j] != grid[i - 1][j]:
                        grid[i - 1][j] = '.'
                if i < len(grid) - 1:
                    if grid[i][j] != grid[i + 1][j]:
                        grid[i + 1][j] = '.'
                if j > 0:
                    if grid[i][j] != grid[i][j - 1]:
                        grid[i][j - 1] = '.'
                if j < len(grid[i]) - 1:
                    if grid[i][j] != grid[i][j + 1]:
                        grid[i][j + 1] = '.'
                grid[i][j] = '.'
    return grid

if __name__ == '__main__':
    fptr = sys.stdout
    r, c, n = map(int, input("input rows, cells, seconds:").split())
    grid = [list(input("enter the row:")) for _ in range(r)]
    grid_after_first_detonation = bomber_man(grid)
    result = [''.join(row) for row in grid_after_first_detonation]
    time.sleep(n)
    fptr.write('\n'.join(result))
    fptr.close()

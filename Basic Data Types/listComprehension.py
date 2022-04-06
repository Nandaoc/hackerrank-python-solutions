## Solution 1 - list comprehensions solution

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    newArr = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(newArr)

## Solution 2 - no list comprehensions solution

# if __name__ == '__main__':
#     x = int(raw_input())
#     y = int(raw_input())
#     z = int(raw_input())
#     n = int(raw_input())
    
#     newArr = []
    
#     for i in range(x + 1):
#         for j in range(y + 1):
#             for k in range(z+1):
#                 if (i+j+k != n):
#                     newArr.append([i, j, k])
#     print(newArr)
    
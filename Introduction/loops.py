## Input Format: the first and only line contains the integer n
## Output Format: print n lines, one corresponding to each i

if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        print(i * i)
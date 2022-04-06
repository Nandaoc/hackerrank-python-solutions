## Input Format: read , the year to test.
## Output Format: the function must return a Boolean value (True/False). Output is handled by the provided code stub.

def is_leap(year):
    leap = False
    
    # Write your logic here
    if((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))
from collections import Counter


def merge_the_tools(string, k):
    count = 0
    list_string = []
    response = ''
    split_s_into = int(len(string)/k)
    aux = int(len(string)/split_s_into)
    aux2 = int(len(string)/split_s_into)
    
    for _ in range(split_s_into):
        letters = Counter(string[count:aux])
        list_string.append(letters)        
        count += aux2
        aux += aux2
    
    for letter in list_string:
        count1 = 0
        for l in letter:
            if count1 <= k - 1:
                response += l
                count1 += 1
        response += '\n'
    
    print(response.strip())

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    new_tuple = tuple(integer_list)
    print(hash(new_tuple))

def minion_game(string):
    string_len = len(string)
    stuart_points = 0
    kevin_points = 0
    for i in range(string_len):
        if string[i] in 'AEIOU':
            kevin_points += string_len - i
        else:
            stuart_points += string_len - i

    if stuart_points == kevin_points:
        print('Draw')
    elif kevin_points > stuart_points:
        print('Kevin',kevin_points)
    else:
        print('Stuart',stuart_points)

if __name__ == '__main__':
    s = input()
    minion_game(s)
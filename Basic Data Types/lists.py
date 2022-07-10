if __name__ == '__main__':
    N = int(input())
    
    numbers = []
    for _ in range(0, N):
        new_command = input()
        steps = new_command.split(' ')
        
        step_one = steps[0]
        if step_one == "insert":
            location = int(steps[1])
            number = int(steps[2])
            numbers.insert(location, number)
        if step_one == "print":
            print(numbers)
        if step_one == "remove":
            number = int(steps[1])
            numbers.remove(number)
        if step_one == "append":
            number = int(steps[1])
            numbers.append(number)
        if step_one == "sort":
            numbers.sort()
        if step_one == "pop":
            numbers.pop()
        if step_one == "reverse":
            numbers.reverse()

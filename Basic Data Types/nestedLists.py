if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
        
    second_lowest_score = sorted(set([score[1] for score in students]))[1]
    names = [student[0] for student in students if student[1] == second_lowest_score]

    print('\n'.join(sorted(names)))

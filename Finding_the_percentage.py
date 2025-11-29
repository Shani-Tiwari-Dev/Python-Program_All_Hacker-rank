if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s_name = student_marks[query_name]
    val = float((s_name[0]+s_name[1]+s_name[2])/3)
    print('%.2f' % val)

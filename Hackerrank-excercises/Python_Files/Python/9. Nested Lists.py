if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if not students.get(score, False):
            students[score] = [name]

        else:
            students[score].append(name)

    print(*sorted(sorted(students.items(), key=lambda x: x[0])[1][1]), sep='\n')




# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
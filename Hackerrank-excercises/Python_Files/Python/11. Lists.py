if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        imps = input().split(' ')
        method = imps[0]

        if len(imps) == 3:
            indx, val = map(int, imps[1:])
            getattr(lst, method)(indx, val)

        elif len(imps) == 2:
            val = int(imps[1]) 
            getattr(lst, method)(val)

        elif method == 'print':
            print(lst)

        else:
            getattr(lst, method)()

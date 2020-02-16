    s = input()
    count = Counter(s)
    for letter, num in sorted(count.most_common(), key=lambda x: (-x[1], x[0]))[:3]:
        print(letter, num)

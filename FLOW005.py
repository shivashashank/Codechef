l = [100, 50, 10, 5, 2, 1]
for i in range(int(input())):
    n = int(input())
    count = 0
    for notes in l:
        count += int(n/notes)
        n = n % notes
        if n == 0:
            break
    print(count)

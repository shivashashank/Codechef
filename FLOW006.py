for i in range(int(input())):
    num = int(input())
    sum = 0
    while(num > 0):
        d = num % 10
        sum = sum+d
        num = num//10
    print(sum)

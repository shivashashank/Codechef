n = int(input())
while n > 0:
    s = list(input())
    l = len(s)
    half = l//2
    a = "".join(sorted(s[:half]))
    if(l % 2 == 0):
        b = "".join(sorted(s[half:]))
    else:
        b = "".join(sorted(s[half+1:]))
    if(a == b):
        print("YES")
    else:
        print("NO")
    n = n-1

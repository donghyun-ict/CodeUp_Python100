a, b, c = map(int, input().split())

def verify(n) :
    if n % 2 == 0 :
        print("even")
    else :
        print("odd")

verify(a)
verify(b)
verify(c)
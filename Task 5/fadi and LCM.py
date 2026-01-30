import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    try:
        line = input().split()
        if not line: return
        x = int(line[0])
    except EOFError:
        return

    ans_a, ans_b = 1, x
    
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            a = i
            b = x // i
            if gcd(a, b) == 1:
                if max(a, b) < max(ans_a, ans_b):
                    ans_a, ans_b = a, b
                    
    print(ans_a, ans_b)

if __name__ == "__main__":
    solve()
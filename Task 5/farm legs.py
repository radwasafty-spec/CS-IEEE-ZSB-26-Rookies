import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    t = int(input_data[0])
    for i in range(1, t + 1):
        n = int(input_data[i])
        if n % 2 != 0:
            print(0)
        else:
            print(n // 4 + 1)

if __name__ == "__main__":
    solve()
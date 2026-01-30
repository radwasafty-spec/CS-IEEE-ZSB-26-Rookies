import sys

def solve():
    MAX = 1000001
    divisors = [0] * MAX

    for i in range(1, MAX):
        for j in range(i, MAX, i):
            divisors[j] += 1

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    results = []
    
    for k in range(1, n + 1):
        x = int(input_data[k])
        results.append(str(divisors[x]))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    ptr = 1
    results = []

    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        
        a = -1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                a = i
                break
        
        if a == -1:
            results.append("NO")
            continue
            
        temp_n = n // a
        b = -1
        for i in range(a + 1, int(temp_n**0.5) + 1):
            if temp_n % i == 0:
                if i != a:
                    b = i
                    break
        
        if b == -1:
            results.append("NO")
            continue
            
        c = temp_n // b
        
        if c > 1 and c != a and c != b:
            results.append(f"YES\n{a} {b} {c}")
        else:
            results.append("NO")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
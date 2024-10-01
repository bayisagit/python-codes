def ilya_and_queries():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    s = data[0]  # the string
    n = len(s)   # length of the string
    m = int(data[1])  # number of queries

    # Preprocess the prefix sums
    prefix = [0] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + (1 if s[i] == s[i - 1] else 0)

    # Prepare to collect answers
    results = []
    for i in range(2, m + 2):
        l, r = map(int, data[i].split())
        results.append(prefix[r - 1] - prefix[l - 1])

    # Print all results
    print("\n".join(map(str, results)))

# Example input
if __name__ == "__main__":
    ilya_and_queries()
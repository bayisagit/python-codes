def can_form_triangle(n, segments):
    segments.sort()  # Sort the segments in ascending order
    
    for i in range(n - 2):  # Check consecutive triples
        if segments[i] + segments[i + 1] > segments[i + 2]:
            return "YES"
    
    return "NO"

# Reading input
def main():
    n = int(input())
    segments = list(map(int, input().split()))
    
    # Output the result
    print(can_form_triangle(n, segments))

if __name__ == "__main__":
    main()

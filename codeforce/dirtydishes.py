def min_washes(n, m, k, meals):
    washes = 0
    for meal in meals:
        if meal == 1:
            if m > 0:
                m -= 1  # Use a clean bowl
            else:
                washes += 1  # Wash a bowl
        else:  # meal == 2
            if k > 0:
                k -= 1  # Use a clean plate
            elif m > 0:
                m -= 1  # Use a clean bowl instead
            else:
                washes += 1  # Wash a plate or bowl
    return washes

# Reading input
def main():
    n, m, k = map(int, input().split())
    meals = list(map(int, input().split()))
    
    # Output the result
    print(min_washes(n, m, k, meals))

if __name__ == "__main__":
    main()
def min_day_to_visit_doctors(n, schedule):
    current_day = 0  # The earliest day Nahom can visit the next doctor
    
    for s, d in schedule:
        if current_day < s:
            current_day = s  # Visit the doctor on their first available day
        else:
            # Find the next available working day for the doctor
            wait_time = (current_day - s + d) // d  # Ceiling division without float
            current_day = s + wait_time * d
    
    return current_day

# Reading input
def main():
    n = int(input())
    schedule = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Output the result
    print(min_day_to_visit_doctors(n, schedule))

if __name__ == "__main__":
    main()

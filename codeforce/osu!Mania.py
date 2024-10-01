def osu_mania_notes(test_cases):
    results = []
    
    for _ in range(test_cases):
        rows = int(input().strip())
        notes_columns = []
        
        for row in range(rows):
            line = input().strip()
            # Find the column of '#' (1-indexed)
            column = line.index('#') + 1
            notes_columns.append(column)
        
        # We want to output from bottom to top, so reverse the list
        results.append(" ".join(map(str, reversed(notes_columns))))
    
    # Print all results for each test case
    print("\n".join(results))

# Read number of test cases
t = int(input().strip())
osu_mania_notes(t)

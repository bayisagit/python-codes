def complete_word(s):
    n = len(s)
    
    # If the string is shorter than 26, we can't form a valid window
    if n < 26:
        print("-1")
        return

    # Sliding window approach: check every substring of length 26
    for i in range(n - 25):  # n - 25 because we need at least 26 characters
        # Frequency array for checking which letters are missing in the window
        freq = [0] * 26
        question_count = 0
        
        # Check the window from index i to i+26
        for j in range(i, i + 26):
            if s[j] == '?':
                question_count += 1
            else:
                index = ord(s[j]) - ord('A')
                freq[index] += 1
        
        # Check if we can fill all missing characters in this window
        missing_count = sum(1 for x in freq if x == 0)
        if question_count == missing_count:
            # We can fill the missing letters with '?' in this window
            result = list(s)
            missing_letters = [chr(i + ord('A')) for i in range(26) if freq[i] == 0]
            missing_idx = 0

            # Replace '?' in the window with missing letters
            for j in range(i, i + 26):
                if result[j] == '?':
                    result[j] = missing_letters[missing_idx]
                    missing_idx += 1
            
            # Replace remaining '?' in the whole string with 'A'
            for k in range(n):
                if result[k] == '?':
                    result[k] = 'A'
            
            print("".join(result))
            return
    
    # If no valid window found
    print("-1")

# Input processing
s = input().strip()
complete_word(s)

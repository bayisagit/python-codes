# Function to check if every cell has an even number of adjacent 'o's
def check_board(n, board):
    # Direction vectors for adjacent cells (left, right, top, bottom)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(n):
        for j in range(n):
            # Count how many adjacent cells contain 'o'
            count_o = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 'o':
                    count_o += 1
            
            # Check if count of 'o's in adjacent cells is even
            if count_o % 2 != 0:
                return "NO"
    
    # If all checks pass, return YES
    return "YES"

# Main function to read the input and call the checker function
def main():
    n = int(input())  # size of the board
    board = [input().strip() for _ in range(n)]  # read the board
    
    # Check the board
    result = check_board(n, board)
    
    # Print the result
    print(result)

# Run the program
if __name__ == "__main__":
    main()

# Function to simulate the game between Nahom and Mikeyas
def main():
    # Read the number of cards
    n = int(input())
    
    # Read the list of card values
    cards = list(map(int, input().split()))
    
    # Initialize scores for Nahom and Mikeyas
    nahom_score = 0
    mikeyas_score = 0
    
    # Two pointers representing the leftmost and rightmost cards
    left = 0
    right = n - 1
    
    # Variable to track whose turn it is (True for Nahom, False for Mikeyas)
    turn_nahom = True
    
    # Simulate the game
    while left <= right:
        # Choose the higher value between the leftmost and rightmost card
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1  # Move the left pointer to the right
        else:
            chosen_card = cards[right]
            right -= 1  # Move the right pointer to the left
        
        # Assign the chosen card to the current player
        if turn_nahom:
            nahom_score += chosen_card
        else:
            mikeyas_score += chosen_card
        
        # Switch turns
        turn_nahom = not turn_nahom
    
    # Output the final scores
    print(nahom_score, mikeyas_score)

# Main entry point for the program
if __name__ == "__main__":
    main()

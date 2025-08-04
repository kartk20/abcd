def calculateTotalPrefix(sequence, k):
    """
    Optimized O(n) solution to count valid non-empty prefix sequences.
    A prefix is valid if we can append 0s/1s to make exactly k "10" subsequences.
    """
    n = len(sequence)
    valid_count = 0
    
    # Track running counts
    ones_count = 0  # Number of 1s seen so far
    current_10_count = 0  # Number of "10" subsequences so far
    
    for i in range(n):
        char = sequence[i]
        
        if char == '1':
            ones_count += 1
        else:  # char == '0'
            current_10_count += ones_count
        
        # Count trailing 1s in current prefix
        trailing_ones = 0
        for j in range(i, -1, -1):
            if sequence[j] == '1':
                trailing_ones += 1
            else:
                break
        
        # Check if current prefix is valid
        if can_make_valid(current_10_count, trailing_ones, k):
            valid_count += 1
    
    return valid_count

def can_make_valid(current_10_count, trailing_ones, k):
    """
    Check if we can make exactly k "10" subsequences by appending digits.
    """
    # If we already have more than k, we can't reduce it
    if current_10_count > k:
        return False
    
    # If we have exactly k, we're good (we can append 1s to maintain k)
    if current_10_count == k:
        return True
    
    # If we have less than k, we need to create more "10" subsequences
    # We can create at most 'trailing_ones' new "10" subsequences by appending 0s
    max_possible = current_10_count + trailing_ones
    
    return max_possible >= k

def calculateTotalPrefixOptimal(sequence, k):
    """
    Fully optimized O(n) solution using precomputed trailing ones.
    """
    n = len(sequence)
    valid_count = 0
    
    # Precompute trailing ones for each position
    trailing_ones = [0] * n
    count = 0
    for i in range(n - 1, -1, -1):
        if sequence[i] == '1':
            count += 1
        else:
            count = 0
        trailing_ones[i] = count
    
    # Track running counts
    ones_count = 0
    current_10_count = 0
    
    for i in range(n):
        char = sequence[i]
        
        if char == '1':
            ones_count += 1
        else:  # char == '0'
            current_10_count += ones_count
        
        # Check if current prefix is valid
        if can_make_valid(current_10_count, trailing_ones[i], k):
            valid_count += 1
    
    return valid_count

# Test both solutions
if __name__ == "__main__":
    test_cases = [
        ("100", 1),
        ("1010", 2),
        ("111", 1),
        ("000", 0),
        ("101010", 3)
    ]
    
    for sequence, k in test_cases:
        result1 = calculateTotalPrefix(sequence, k)
        result2 = calculateTotalPrefixOptimal(sequence, k)
        print(f"Sequence: '{sequence}', k={k}")
        print(f"  Result (basic): {result1}")
        print(f"  Result (optimal): {result2}")
        print(f"  Match: {result1 == result2}")
        print()
        
        # Detailed trace for the example
        if sequence == "100" and k == 1:
            print("Detailed trace for '100', k=1:")
            ones_count = 0
            current_10_count = 0
            
            for i in range(len(sequence)):
                char = sequence[i]
                prefix = sequence[:i+1]
                
                if char == '1':
                    ones_count += 1
                else:
                    current_10_count += ones_count
                
                # Count trailing ones
                trailing_ones = 0
                for j in range(i, -1, -1):
                    if sequence[j] == '1':
                        trailing_ones += 1
                    else:
                        break
                
                valid = can_make_valid(current_10_count, trailing_ones, k)
                print(f"  Prefix '{prefix}': 10_count={current_10_count}, trailing_1s={trailing_ones}, valid={valid}")
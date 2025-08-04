def calculateTotalPrefix(sequence, k):
    """
    Count the number of valid non-empty prefix sequences.
    
    A prefix is valid if we can append 0s and/or 1s to make exactly k "10" subsequences.
    
    Algorithm:
    1. For each prefix, count existing "10" subsequences
    2. Count trailing 1s (these can form new "10"s with appended 0s)
    3. Check if we can reach exactly k "10" subsequences
    
    Time Complexity: O(n²) due to trailing ones calculation
    Space Complexity: O(1)
    
    Args:
        sequence (str): Binary string of 0s and 1s
        k (int): Target number of "10" subsequences
        
    Returns:
        int: Number of valid non-empty prefix sequences
    """
    n = len(sequence)
    valid_count = 0
    
    # Track running counts as we process each character
    ones_count = 0      # Number of 1s seen so far
    current_10_count = 0  # Number of "10" subsequences so far
    
    for i in range(n):
        char = sequence[i]
        
        # Update counts based on current character
        if char == '1':
            ones_count += 1
        else:  # char == '0'
            # Each 0 forms a "10" with all previous 1s
            current_10_count += ones_count
        
        # Count trailing 1s in current prefix
        trailing_ones = 0
        for j in range(i, -1, -1):
            if sequence[j] == '1':
                trailing_ones += 1
            else:
                break
        
        # Check if current prefix can be made valid
        if can_make_valid(current_10_count, trailing_ones, k):
            valid_count += 1
    
    return valid_count


def can_make_valid(current_10_count, trailing_ones, k):
    """
    Check if we can make exactly k "10" subsequences by appending digits.
    
    Logic:
    - If current_10_count > k: impossible (can't reduce "10" count)
    - If current_10_count == k: valid (append 1s to maintain count)
    - If current_10_count < k: valid if we can create enough new "10"s
      by appending 0s after the trailing 1s
    
    Args:
        current_10_count (int): Current number of "10" subsequences
        trailing_ones (int): Number of consecutive 1s at end of prefix
        k (int): Target number of "10" subsequences
        
    Returns:
        bool: True if we can make exactly k "10" subsequences
    """
    # Case 1: Already too many "10" subsequences
    if current_10_count > k:
        return False
    
    # Case 2: Exactly k "10" subsequences - we can maintain this by appending 1s
    if current_10_count == k:
        return True
    
    # Case 3: Need more "10" subsequences
    # We can create at most 'trailing_ones' new "10"s by appending 0s
    max_possible = current_10_count + trailing_ones
    return max_possible >= k


# Optimized O(n) version
def calculateTotalPrefixOptimized(sequence, k):
    """
    Optimized O(n) solution using precomputed trailing ones.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(sequence)
    if n == 0:
        return 0
    
    # Precompute trailing ones for each position
    trailing_ones = [0] * n
    count = 0
    for i in range(n - 1, -1, -1):
        if sequence[i] == '1':
            count += 1
        else:
            count = 0
        trailing_ones[i] = count
    
    valid_count = 0
    ones_count = 0
    current_10_count = 0
    
    for i in range(n):
        char = sequence[i]
        
        if char == '1':
            ones_count += 1
        else:
            current_10_count += ones_count
        
        if can_make_valid(current_10_count, trailing_ones[i], k):
            valid_count += 1
    
    return valid_count


if __name__ == "__main__":
    # Test with the provided example
    sequence = "100"
    k = 1
    
    result = calculateTotalPrefix(sequence, k)
    print(f"Example: sequence='{sequence}', k={k}")
    print(f"Result: {result}")
    print()
    
    # Verify with step-by-step trace
    print("Step-by-step analysis:")
    print("Prefix '1': has 0 '10's, 1 trailing 1 -> can make 0+1=1 '10's -> VALID")
    print("Prefix '10': has 1 '10', 0 trailing 1s -> already has k=1 '10's -> VALID") 
    print("Prefix '100': has 2 '10's, 0 trailing 1s -> has more than k=1 -> INVALID")
    print()
    print("Therefore, 2 prefixes are valid.")
    
    # Additional test cases
    test_cases = [
        ("1010", 2),
        ("111", 1), 
        ("000", 0),
        ("1", 0),
        ("10101", 3)
    ]
    
    print("\nAdditional test cases:")
    for seq, target_k in test_cases:
        result1 = calculateTotalPrefix(seq, target_k)
        result2 = calculateTotalPrefixOptimized(seq, target_k)
        print(f"'{seq}', k={target_k}: {result1} (optimized: {result2})")
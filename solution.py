def calculateTotalPrefix(sequence, k):
    """
    Count the number of valid non-empty prefix sequences.
    A prefix is valid if we can append 0s/1s to make exactly k "10" subsequences.
    """
    n = len(sequence)
    valid_count = 0
    
    for prefix_len in range(1, n + 1):
        prefix = sequence[:prefix_len]
        
        # Count existing "10" subsequences in the prefix
        current_10_count = count_10_subsequences(prefix)
        
        # Count trailing 1s in the prefix (these can form new "10"s with appended 0s)
        trailing_ones = count_trailing_ones(prefix)
        
        # Check if this prefix can be made valid
        if can_make_valid(current_10_count, trailing_ones, k):
            valid_count += 1
    
    return valid_count

def count_10_subsequences(s):
    """Count the number of "10" subsequences in string s"""
    count = 0
    ones_seen = 0
    
    for char in s:
        if char == '1':
            ones_seen += 1
        else:  # char == '0'
            count += ones_seen
    
    return count

def count_trailing_ones(s):
    """Count the number of consecutive 1s at the end of string s"""
    count = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            count += 1
        else:
            break
    return count

def can_make_valid(current_10_count, trailing_ones, k):
    """
    Check if we can make exactly k "10" subsequences by appending digits.
    
    current_10_count: existing "10" subsequences in prefix
    trailing_ones: number of 1s at the end of prefix
    k: target number of "10" subsequences
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

# Test with the example
if __name__ == "__main__":
    # Example: sequence = "100", k = 1
    sequence = "100"
    k = 1
    result = calculateTotalPrefix(sequence, k)
    print(f"For sequence '{sequence}' and k={k}, result = {result}")
    
    # Let's trace through each prefix:
    print("\nTracing through prefixes:")
    for i in range(1, len(sequence) + 1):
        prefix = sequence[:i]
        current_10 = count_10_subsequences(prefix)
        trailing_ones = count_trailing_ones(prefix)
        valid = can_make_valid(current_10, trailing_ones, k)
        print(f"Prefix '{prefix}': current_10={current_10}, trailing_ones={trailing_ones}, valid={valid}")
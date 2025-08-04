def calculateTotalPrefix(sequence, k):
    """Count valid non-empty prefix sequences."""
    n = len(sequence)
    valid_count = 0
    
    ones_count = 0
    current_10_count = 0
    
    print(f"Analyzing sequence '{sequence}' with k={k}")
    print("=" * 50)
    
    for i in range(n):
        char = sequence[i]
        prefix = sequence[:i+1]
        
        if char == '1':
            ones_count += 1
        else:  # char == '0'
            current_10_count += ones_count
        
        # Count trailing 1s
        trailing_ones = 0
        for j in range(i, -1, -1):
            if sequence[j] == '1':
                trailing_ones += 1
            else:
                break
        
        # Check validity
        valid = can_make_valid(current_10_count, trailing_ones, k)
        if valid:
            valid_count += 1
            
        print(f"Prefix '{prefix}': current_10s={current_10_count}, trailing_1s={trailing_ones}, valid={valid}")
    
    print("=" * 50)
    print(f"Total valid prefixes: {valid_count}")
    return valid_count

def can_make_valid(current_10_count, trailing_ones, k):
    """Check if we can make exactly k '10' subsequences."""
    if current_10_count > k:
        return False
    if current_10_count == k:
        return True
    max_possible = current_10_count + trailing_ones
    return max_possible >= k

if __name__ == "__main__":
    # Test the specific case
    sequence = "00111"
    k = 1
    result = calculateTotalPrefix(sequence, k)
    
    print(f"\nExplanation:")
    print("- Prefixes '0', '00': Have 0 '10's and 0 trailing 1s -> can't reach k=1 -> INVALID")
    print("- Prefix '001': Has 0 '10's and 1 trailing 1 -> can make 0+1=1 '10's -> VALID")
    print("- Prefix '0011': Has 0 '10's and 2 trailing 1s -> can make 0+2=2 '10's (≥1) -> VALID") 
    print("- Prefix '00111': Has 0 '10's and 3 trailing 1s -> can make 0+3=3 '10's (≥1) -> VALID")
    print(f"\nAnswer: {result} valid prefixes")
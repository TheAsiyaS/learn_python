# #loop : fizz, buzz problem

# n = int(input("Enter a number :"))
# total = 0

# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FIZZBUZZ")
#     elif i % 3 == 0:
#         print("FIZZ")
#     elif i % 5 == 0:
#         print("BUZZ")
#     else:
#         print(i)
#         total += i

# print("Sum:", total)

def longest_palindrome(s: str) -> str:
    if not s:
        return ""
        
    start, end = 0, 0
    
    # Helper function to expand around a center
    def expand_around_center(left: int, right: int) -> int:
        # Loop expands outward as long as conditions match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Returns the length of the valid palindrome found
        return right - left - 1

    # Main loop treating each index as a center
    for i in range(len(s)):
        # Case 1: Odd-length palindromes (e.g., "aba", center is 'b')
        len1 = expand_around_center(i, i)
        
        # Case 2: Even-length palindromes (e.g., "abba", center is between 'b' and 'b')
        len2 = expand_around_center(i, i + 1)
        
        # Track the maximum length found
        max_len = max(len1, len2)
        
        # Update tracking pointers if a longer palindrome is found
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]


## Encode and Decode Strings

### Problem
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode` methods.

### Brute Force
- Join strings with a special delimiter (e.g., comma)
- But this fails if the delimiter appears in the strings
- Time: O(n) where n is total characters
- Space: O(n)

### Optimized Approach
- For encoding: Store lengths of each string separated by commas, followed by '#', then concatenate all strings
- For decoding: Parse the lengths from the beginning until '#', then extract strings using the lengths

### Complexity
- Time: O(n) for both encode and decode
- Space: O(n) for the encoded string

### Key Learning
- Length-based encoding avoids delimiter collision issues
- Parsing variable-length data requires careful index management
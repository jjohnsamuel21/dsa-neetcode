## Valid Sudoku

### Problem
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need to be validated.

### Brute Force
- For each row, check for duplicates using a set
- For each column, check for duplicates using a set
- For each 3x3 sub-box, check for duplicates using a set
- Time: O(1) since board is fixed size 9x9
- Space: O(1)

### Optimized Approach
- Use a single HashMap with keys for rows, columns, and sub-boxes
- For each cell, check if the number already exists in its row, column, or sub-box
- If not, add it to the respective lists

### Complexity
- Time: O(1) since 81 cells
- Space: O(1) for the hash map

### Key Learning
- HashMap can track multiple constraints simultaneously
- Sub-box indexing requires careful calculation
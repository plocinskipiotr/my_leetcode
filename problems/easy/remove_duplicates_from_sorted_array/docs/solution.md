# Solution
*   Set pointer k as 0
*   Traverse through elements of an array
    - if element[i] > element[k]
        - swap nums[k+1] with nums[i]
        - increment k
*   Return k+1
# Complexity
| Memory | Runtime |
|--------|---------|
| O(n)   | O(n)    |
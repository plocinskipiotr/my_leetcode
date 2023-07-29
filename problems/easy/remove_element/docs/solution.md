# Solution
* Create pointer i to the first element of array
* Traverse through array
  - if element value is not equal val:
    - replace element with index i with actual value
    - increment i
* return i

This algorithm will in effect pop all occurrences by replacing

# Complexity
| Memory | Runtime |
|--------|---------|
| O(n)   | O(n)    |

# Hint
*   Think how to delete the occurrences of val without using .pop()
*   Replace the pop() operation with replacement
*   Do not overcomplicate
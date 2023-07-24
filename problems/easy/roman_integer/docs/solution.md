# Solution
*   create decoding dictionary to translate single roman character to integer value
*   initialise accumulator variable with 0
*   traverse through elements of an array until the one before last
    - if value of next element > value of current element:
      - subtract element value from accumulator
    - otherwise
      - add element value to accumulator
* add the last array element to accumulator

# Complexity
| Memory | Runtime |
|--------|---------|
| O(n)   | O(n)    |

# Hints
*   to prevent IndexError iterate to the one before last element of array
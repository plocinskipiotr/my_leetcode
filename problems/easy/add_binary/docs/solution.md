# Solution
*   determine the longer sequence
*   add addition neutral elements ('0') to shorter sequence to make it as long as longer sequence
*   initialize the result sequence with '0' and make it as long as longer sequence
*   iterate through longer sequence in reversed order
    - determine the result digit starting from the end of result
      - if the sum of sequences and carry:
        - equals 0; set digit as 0 carry as 0
        - equals 1; set digit as 1 carry as 0
        - equals 2; set digit as 0 carry as 1
        - equals 3; set digit as 1 carry as 1
*   convert the result to string
    -  if carry equals 1 put 1 at the beginning of the result
*   return result

# Complexity
| Memory | Runtime |
|--------|---------|
| O(n)   | O(n)    |
# Solution
*   Append the element of the list to the stack taking into account, following rules:
    - if element is an open bracket, push it to a stack
    - if stack is not empty try to pair up element (it must be a closed bracket) with bracket on a top of the stack
    - otherwise (element is neither open bracket nor a closed, which doesn't pair up with this stored at a top of the stack) sequence is invalid

# Complexity
| Memory | Runtime |
|--------|---------|
| O(n)   | O(n)    |
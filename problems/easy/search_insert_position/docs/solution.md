# Solution
*   create two pointers set to the beginning and end of array __(l,r)__
*   while __l__ is less or equal __r__
    -  determine the __middle element__ of array
    -  check if middle element is less than the target
       - if yes set __r__ as middle element - 1
    -  check if middle element is greater than the target
       - if yes set __l__ as middle element + 1
    -  check if middle element equals the target
       - if yes return the index of middle element
*   if the element hasn't been found in the array
    -  return index equals l

    
# Complexity
| Memory | Runtime  |
|--------|----------|
| O(n)   | O(log n) |
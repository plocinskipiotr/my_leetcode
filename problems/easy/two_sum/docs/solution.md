# Solution
*   Traverse through elements of an array
    - if __element__ is in __dictionary keys__
      - return [_iteration_index_, _difference_index_] 
    - else
      - calculate __difference__ between __target__ and __element__
      - add __difference__ as a key and __index__ as a value

# Complexity
| Memory | Runtime |
|--------|---------|
| O(n)   | O(n)    |

# Hints
*   target = el_x + el_y <==> el_y = target - el_x
*   diff = target-el_x
*   dictionary lookup ~0(1)
*   set cannot be used because of index
# Solution
*   set the first string from the array as a reference string
    - iterate in range of the length of the reference string
      - set the reference character as the character placed in string under current iteration index
          - iterate through the words in the array omitting the reference; for each string:
            - check if either:
              - the index of iteration range is lesser or equal than the length of the word; </br> 
              - check if the character in the word under given index is different as reference character;
            - if one of above conditions is fulfilled
              - return the reference sequence to one before last index </br> 
    - if the iteration of the reference string is accomplished; return the reference string
# Complexity
| Memory | Runtime |
|--------|---------|
| O(n)   | O(n)    |

# Hints
*   corner case: there is no elements in given array of strings
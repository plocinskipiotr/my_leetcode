# Solution
*   Create helper ListNode with neutral value (0), it will be omitted in the final result
*   Set the current pointer to the ListNode()
*   Traverse through the lists until one of them terminates
    - compare the value of the nodes
    - if the value of current element of list1 > list2
      - move the current next pointer to list1
      - advance the list1 pointer to the next element of list1
    - else
      - move the current next pointer to list2
      - advance the list2 pointer to the next element of list2
    - advance the current next pointer to the next element 
*   If one of the lists ends:
    - point the current next pointer to the list which didn't end
    - return the pointer to next element of helper ListNode

# Complexity
| Memory | Runtime |
|------|-------|
| O(n) | O(n)  |

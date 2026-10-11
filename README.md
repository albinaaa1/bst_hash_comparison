
# BST vs Hash Table Performance Comparison

## 1. Introduction

The goal of this project is to implement a Binary Search Tree
(BST) and a Hash Table and compare their performance.

Both data structures support insertion, searching, and deletion,
but they organize data differently.

## 2. Implementation

The BST stores smaller keys in the left subtree and larger keys
in the right subtree. It is implemented without automatic balancing.

The Hash Table uses separate chaining. Each bucket stores a list
of keys that have the same hash index.

## 3. Time Complexity

| Operation | BST Average | BST Worst | Hash Table Average | Hash Table Worst |
|---|---|---|---|---|
| Insertion | O(log n) | O(n) | O(1) | O(n) |
| Search | O(log n) | O(n) | O(1) | O(n) |
| Deletion | O(log n) | O(n) | O(1) | O(n) |

The average BST complexity assumes a reasonably balanced tree.
The average Hash Table complexity assumes good key distribution
and a controlled load factor.

## 4. Experimental Results

The structures were tested with 100, 1,000, and 10,000 elements.
Each operation was measured three times, and the average duration
was recorded in seconds.

The actual measurements from results.csv below.

| Structure | Elements | Operation | Time (seconds) |
|Testing 100 elements|---:|---|---:|
| BST | 100 | Insert | 0.001567 seconds |
| BST | 100 | Search | 0.000074 seconds |
| BST | 100 | Delete | 0.000133 seconds |
| Hash Table | 100 | Insert | 0.000033 seconds |
| Hash Table | 100 | Search | 0.000027 seconds |
| Hash Table | 100 | Delete | 0.000032 seconds |

Testing 1000 elements
BST        | insert | 0.001567 seconds
BST        | search | 0.001353 seconds
BST        | delete | 0.002501 seconds
Hash Table | insert | 0.000306 seconds
Hash Table | search | 0.000278 seconds
Hash Table | delete | 0.000367 seconds

Testing 10000 elements
BST        | insert | 0.028816 seconds
BST        | search | 0.018002 seconds
BST        | delete | 0.029166 seconds
Hash Table | insert | 0.002823 seconds
Hash Table | search | 0.002088 seconds
Hash Table | delete | 0.002496 seconds

## 5. Discussion

The experimental results show that the performance of a BST and a Hash Table depends on the number of elements and the way data is stored. A Hash Table usually performs insertion, searching, and deletion faster because these operations take O(1) time on average when keys are distributed well and the table has enough capacity.

A BST can also perform efficiently when its structure is balanced. However, the implemented BST does not use balancing, so its performance depends on the order of insertion. If the tree becomes unbalanced, operations may take O(n) time. As the number of elements increases from 100 to 10,000, the execution times may also increase.

For small datasets, the difference between the two structures may be very small. For larger datasets, the Hash Table may show better performance for the tested operations. However, actual results depend on the computer, the implementation, and the distribution of keys. The measured execution times should be used to determine which structure performed better in this experiment.

## 6. Conclusion

In conclusion, both the Binary Search Tree and the Hash Table are useful data structures, but they have different advantages. The Hash Table is a good choice when fast insertion, searching, and deletion are important. The BST is useful when data needs to be stored in sorted order and when ordered traversal is required.

The experiment helps demonstrate the difference between theoretical time complexity and practical performance. A Hash Table provides O(1) average-time operations under suitable conditions, while a normal BST has O(log n) average-time operations when reasonably balanced and O(n) worst-case operations. Therefore, the best choice depends on the requirements of the application and the actual test results.


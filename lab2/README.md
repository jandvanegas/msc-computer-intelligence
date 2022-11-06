# Lab 1: Set Covering

## Task

Given a number $N$ and some lists of integers $P = (L_0, L_1, L_2, ..., L_n)$, 
determine, if possible, $S = (L_{s_0}, L_{s_1}, L_{s_2}, ..., L_{s_n})$
such that each number between $0$ and $N-1$ appears in at least one list

$$\forall n \in [0, N-1] \ \exists i : n \in L_{s_i}$$

and that the total numbers of elements in all $L_{s_i}$ is minimum. 

## Approach
My approach was to take the length of number of unique intergers in the 
individual. Individuals in the population start with just one gene (one list of integers),
and in the crossover, I set up a random condition to add or remove a gene.

To test with N=5, run the script like:
```bash
python main.py 5
```

## Results
| N             | Solution Number of Elements  | Iterations    |
| ------------- | ---------------------------- | ------------- |
| 5             | not found                    |               |
| 10            | 5                            | 14            |
| 20            | 6                            | 23            |
| 100           | 8                            | 44            |
| 500           | 11                           | 97            |
| 1000          | 12                           | 147           |


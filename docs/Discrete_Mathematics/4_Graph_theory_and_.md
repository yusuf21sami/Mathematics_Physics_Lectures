## Graph representation

### Task 1

We have 3 ways to represent a graph:

- Edge list plus vertex set
- Adjacency matrix
- Adjacency list

For each graph listed below, complete the other two methods of graph representation and draw the graph.

#### Graph 1

Undirected graph

```python
[(1, 3), (1, 4), (1, 5), (2, 6), (3, 6), (4, 5)]
```

#### Graph 2

Undirected graph


```python
[[0 0 1 0 0 0]
 [0 0 0 0 0 0]
 [1 0 0 0 1 1]
 [0 0 0 0 1 0]
 [0 0 1 1 0 1]
 [0 0 1 0 1 0]]
```

#### Graph 3

Undirected graph

```python
{1: [4], 2: [4], 3: [5, 6], 4: [1, 2, 6], 5: [3], 6: [3, 4]}
```

#### Graph 4

Directed graph

```python
[(1, 2), (2, 5), (3, 4), (4, 1), (5, 2), (5, 3), (6, 3), (6, 5)]
```

#### Graph 5

Directed graph

```python
[[0 1 0 1 0 1]
 [0 0 0 0 0 0]
 [0 1 0 0 1 0]
 [1 0 0 0 1 0]
 [1 0 0 1 0 1]
 [0 1 0 1 1 0]]
```

#### Graph 6

Directed graph

```python
{1: [2, 6], 2: [1, 4], 3: [4, 5], 4: [1, 6], 5: [2, 3], 6: [1, 3, 5]}
```

### Task 2  

For following graph

```python
0: [1, 2],
1: [3, 4, 5],
2: [0, 3, 4, 7, 8],
3: [0, 1, 6],
4: [1, 2, 9],
5: [1, 3, 8, 9],
6: [3, 5, 7, 9],
7: [2, 8],
8: [2, 5, 7],
9: [6],
```

- Find the shortest path from vertex 0 to vertex 9 using Dijkstra's algorithm.
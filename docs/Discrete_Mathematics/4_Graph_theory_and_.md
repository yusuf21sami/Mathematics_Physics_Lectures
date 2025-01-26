## Useful links

* [https://csacademy.com/app/graph_editor/](https://csacademy.com/app/graph_editor/)
* [https://graphonline.top/](https://graphonline.top/)
* [https://d3gt.com/unit.html](https://d3gt.com/unit.html)
* [https://networkx.org/documentation/stable/index.html](https://networkx.org/documentation/stable/index.html)
* [https://pyvis.readthedocs.io/en/latest/index.html](https://pyvis.readthedocs.io/en/latest/index.html)
 

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
{1: [4],
 2: [4], 
 3: [5, 6], 
 4: [1, 2, 6], 
 5: [3], 
 6: [3, 4]}
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
*Task
#### Graph 6

Directed graph

```python
{1: [2, 6], 
 2: [1, 4], 
 3: [4, 5], 
 4: [1, 6], 
 5: [2, 3], 
 6: [1, 3, 5]}
```

### Task 2  

For the following undirected graph:


```python
    1: [3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [6, 7],
    5: [6, 2],
    6: [4, 5],
    7: [8],
    8: [7]
```

Answer the following questions:

1. How many vertices and edges are there in the graph?
2. Is the graph connected? Justify your answer.
3. What is the diameter of the graph?
4. What is the radius of the graph?
5. Which vertex (or vertices) is in the center of the graph?
6. Is the graph Eulerian? Why or why not?
7. Find the degree of vertex 4.
8. Find the shortest path from vertex 5 to vertex 8 using Dijkstra's algorithm.
9. What is the length of the shortest path from vertex 5 to vertex 8?
10. Does the graph contain a cycle? If yes, what is the length of one cycle?


### Task 3

Consider above graph again, but this time, consider the graph as a directed graph.

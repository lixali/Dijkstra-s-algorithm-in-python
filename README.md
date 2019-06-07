# Dijkstra-s-algorithm-in-python

In the Dijkstra_python.py file, the shortest path will be found in the following diagram.



![Alt text](Dijkstra_algorithm_shortest_path.png?raw=true "Optional Title")



This funtion will take three inputs (input diagram, starting point, end point), and print out the shortest distance and shortest path. 

For studying purpose:

(1)Just run the code("Dijkstra_python.py") in the Python3 environment, and it will output without any errors (the code is outputing the shortest distance and shortest path between "A" and "E").

(2) To calculate the distance of different startpoint and endpoint, change the last line of code.
For example, to calculate the shortest distance and shortest path between "A" and "D", change the last line of code to "dijkstra(graph, 'a', 'd')"

(3) After the code runs without any errors, go through and understand the code and comment line by line and do time and space complexity analysis. THe code is using iterative approach (using a priority "queue"(in this case, it is a hash table to compare abd get the least value in the hash table to serve as priority queue) to store unseen nodes and pop them out). Because Dijkstra algorithm is an advanced version of Breach First Search(BFS), the time complexity is O(v) and the sapce complexity is also O(v)  (v is number of nodes). 

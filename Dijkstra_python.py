graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}} ### this dictionary represent the above graph
 
def dijkstra(graph,start,goal):
    shortest_distance = {}   ### this hash table will hold the shortest distance value of each node
    predecessor = {}         ### this hash table will hold the previous node from which the shortest distance is calculated
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0     ### the "start" node shortest distance is 0, all the other nodes are infinity (it is 9999999 here)
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node    
            elif shortest_distance[node] < shortest_distance[minNode]:   ### to find the node with the smallest distance and name that node "minNode"
                minNode = node            ### the minMode will be used in the following for loop to update its "childNode"
                                          ### in the beginning, the minNode will be "start" node because start node shortest distance is 0 while others are infinity

        for childNode, weight in unseenNodes[minNode].items():  ### this is to update shortest distance of the child nodes of the minNode (childNode is the adjacent node of the minNode)
            if childNode in unseenNodes:   ### the seen nodes must have already found the shortest path, therefore only unseen nodes' distance should be updated 
                if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                    shortest_distance[childNode] = weight + shortest_distance[minNode]  ### if the child node is unseen node, and its new shortest distance is found, the hash table "shortest_distance" will be updated 
                    predecessor[childNode] = minNode  ### this is to keep track the previous node from which the shortest distance is calculated
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
 
 
dijkstra(graph, 'a', 'e')

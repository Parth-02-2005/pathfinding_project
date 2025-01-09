def create_graph(vertices, edges):
    """
    Create an adjacency list representation of the graph.
    :param vertices: Number of vertices
    :param edges: List of edges as [u, v, w]
    :return: Adjacency list
    """
    adj_list = {i: [] for i in range(vertices)}
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    return adj_list


def dijkstra(graph, vertices, src):
    """
    Implementation of Dijkstra's algorithm.
    :param graph: Adjacency list of the graph
    :param vertices: Number of vertices
    :param src: Source node
    :return: List of distances and previous nodes
    """
    import heapq

    dist = {i: float('inf') for i in range(vertices)}
    prev = {i: None for i in range(vertices)}
    dist[src] = 0

    priority_queue = [(0, src)]  # (distance, node)

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist, prev

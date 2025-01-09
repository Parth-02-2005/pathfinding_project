from flask import Flask, render_template, request, jsonify
import networkx as nx
from algorithms.dijkstra import create_graph, dijkstra

app = Flask(__name__)

# Graph data
GRAPH_DATA = {
    "vertices": 9,
    "edges": [
        [0, 1, 4], [0, 7, 8], [1, 7, 11], [1, 2, 8],
        [7, 8, 7], [6, 7, 1], [2, 8, 2], [6, 8, 6],
        [5, 6, 2], [2, 5, 4], [2, 3, 7], [3, 5, 14],
        [3, 4, 9], [4, 5, 10]
    ]
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/graph', methods=['GET'])
def get_graph():
    """
    Generate the graph structure and positions using NetworkX.
    """
    G = nx.Graph()
    for edge in GRAPH_DATA['edges']:
        G.add_edge(edge[0], edge[1], weight=edge[2])

    # Get positions using a layout
    pos = nx.spring_layout(G)  # Can use other layouts like circular_layout or shell_layout

    # Convert positions and edges to a JSON-friendly format
    nodes = [{"id": node, "label": str(node), "x": pos[node][0] * 1000, "y": pos[node][1] * 1000}
             for node in G.nodes]
    edges = [{"from": u, "to": v, "label": str(G[u][v]['weight']), "arrows": "to"}
             for u, v in G.edges]

    return jsonify({"nodes": nodes, "edges": edges})


@app.route('/solve', methods=['POST'])
def solve():
    """
    Solve the graph using Dijkstra's algorithm and return the shortest path to the target.
    """
    data = request.json
    src = int(data.get("source", 0))
    target = int(data.get("target", -1))  # Get the target node (-1 means no specific target)

    vertices = GRAPH_DATA["vertices"]
    edges = GRAPH_DATA["edges"]

    graph = create_graph(vertices, edges)
    distances, prev = dijkstra(graph, vertices, src)

    # Reconstruct the shortest path
    path = []
    if target != -1:  # Only calculate the path if a target is specified
        current = target
        while current is not None:
            parent = prev[current]
            if parent is not None:
                path.append((parent, current))  # Add the edge to the path
            current = parent

    path.reverse()  # Reverse the path to go from source to target

    return jsonify({
        "distances": distances,
        "path": path  # Only return the edges in the shortest path
    })



if __name__ == '__main__':
    app.run(debug=True)
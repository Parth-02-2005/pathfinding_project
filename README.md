Pathfinding Visualizer with Dijkstra's Algorithm

Overview:

This project is an interactive Pathfinding Visualizer that demonstrates the functionality of Dijkstra's Algorithm for finding the shortest path in a weighted graph. It features a dynamic graph visualization built using the vis-network library on the frontend and a Flask backend powered by NetworkX for graph handling and shortest path calculations.

Features:

1. Interactive Graph Visualization:
Nodes and edges are dynamically rendered on a responsive graph.
Weights represent travel times between nodes.
2. Shortest Path Calculation:
Implements Dijkstra's Algorithm to find and highlight the shortest path from a source to a target node.
Supports interactive input for source and target nodes.
3. Dynamic Edge and Node Styling:
Highlights the shortest path edges in red.
Customizable node and edge styles for clear visualization.
4. Responsive Design:
Works seamlessly across different screen sizes with an adaptive layout.

Technologies Used:
Frontend:
HTML/CSS: For the layout and styling of the application.
vis-network: JavaScript library for rendering and interacting with the graph.
Axios: For seamless communication with the backend.

Backend:
Flask: Lightweight Python web framework for handling requests and responses.
NetworkX: Library for graph representation, layout generation, and shortest path calculations.

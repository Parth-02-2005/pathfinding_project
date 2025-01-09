let network = null;

// Fetch and render the graph
function renderGraph() {
    axios.get('/graph')
        .then(response => {
            const data = response.data;

            // Create a vis-network dataset
            const nodes = new vis.DataSet(data.nodes);
            const edges = new vis.DataSet(data.edges);

            // Network options
            // const options = {
            //     nodes: {
            //         shape: 'dot',
            //         size: 20,
            //         font: { size: 15 },
            //         borderWidth: 2,
            //     },
            //     edges: {
            //         font: { size: 12, align: 'middle' },
            //         color: { color: '#848484' },
            //     },
            //     physics: {
            //         enabled: true,
            //     },
            // };
            const options = {
                nodes: {
                    shape: 'dot',
                    size: 20,
                    font: { size: 17, color: "#8d05fc"},
                    borderWidth: 2,
                },
                edges: {
                    font: { size: 15, align: 'middle' },
                    color: { color: '#848484' },
                    smooth: {
                        type: 'dynamic', // Adjust to fit within the container
                    },
                },
                physics: {
                    enabled: true,
                },
                interaction: {
                    hover: true, // Allow smoother interactions
                    zoomView: true, // Enable zooming for larger graphs
                },
            };
            

            // Render the network
            const container = document.getElementById('network');
            network = new vis.Network(container, { nodes, edges }, options);
        })
        .catch(error => {
            console.error("Error loading the graph:", error);
        });
}

// Solve the graph and highlight the shortest path
function solveGraph() {
    const source = prompt("Enter the source node (0-8):");
    const target = prompt("Enter the target node (0-8):");

    axios.post('/solve', { source: source, target: target })
        .then(response => {
            const data = response.data;
            const shortestPathEdges = data.path; // Get the shortest path edges

            // Highlight only the shortest path edges
            const edges = network.body.data.edges.get();
            const updatedEdges = edges.map(edge => {
                const isPathEdge = shortestPathEdges.some(
                    pathEdge => (pathEdge[0] === edge.from && pathEdge[1] === edge.to) ||
                                (pathEdge[0] === edge.to && pathEdge[1] === edge.from)
                );

                return {
                    ...edge,
                    color: isPathEdge
                        ? { color: '#FF0000', highlight: '#FF4500', hover: '#FF6347' } // Red for shortest path
                        : { color: '#848484' }, // Default edge color
                    width: isPathEdge ? 4 : 1, // Thicker edges for the path
                };
            });

            network.body.data.edges.update(updatedEdges);

            alert("Shortest path highlighted in red!");
        })
        .catch(error => {
            console.error("Error solving the graph:", error);
        });
}


// Attach event listeners
document.getElementById('generateGraph').addEventListener('click', renderGraph);
document.getElementById('solve').addEventListener('click', solveGraph);

// Render the graph on page load
renderGraph();
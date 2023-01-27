from algorithm_practice.graphs.graph import Graph

def test_bgs_one_item():
    graph = Graph({"Seattle": []})

    visited = graph.bfs()

    assert visited == ["Seattle"]

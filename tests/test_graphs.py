from algorithm_practice.graphs.graph import Graph, possible_bipartition

def test_bgs_one_item():
    graph = Graph({"Seattle": []})

    visited = graph.bfs()

    assert visited == ["Seattle"]


def test_get_components_valid_graph():
    # arrange
    g = Graph( {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
        "D": ["E"],
        "E": ["D"],
        "F": []
    })
    # act
    result = g.components()

    # assert
    assert result == [["A", "B", "C"], ["D", "E"], ["F"]]

def test_get_components_one_item_graph():
    graph = Graph({"A": []})

    visited = graph.components()

    assert visited == [["A"]]

def test_possible_bipartition_true_non_empty_input():
    # arrange
    dislikes = { 
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Cooper": ["Nala", "Bruno"],
        "Spot": ["Nala"],
        "Bruno": ["Cooper"]
    }
    # act
    result = possible_bipartition(dislikes)

    # assert
    assert result == True

def test_possible_bipartition_empty_input():
    # arrange
    dislikes = {}
    # act
    result = possible_bipartition(dislikes)

    # assert
    assert result == True


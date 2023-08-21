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

def test_example_1():
    # Arrange
    dislikes = {
      "Fido": [],
      "Rufus": ["James", "Alfie"],
      "James": ["Rufus", "T-Bone"],
      "Alfie": ["Rufus"],
      "T-Bone": ["James"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert answer

def test_example_2():
    dislikes = {
      "Fido": [],
      "Rufus": ["James", "Alfie"],
      "James": ["Rufus", "Alfie"],
      "Alfie": ["Rufus", "James"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer

def test_example_3():
    # Arrange
    dislikes = {
      "Fido": [],
      "Rufus": ["James", "Scruffy"],
      "James": ["Rufus", "Alfie"],
      "Alfie": ["T-Bone", "James"],
      "T-Bone": ["Alfie", "Scruffy"],
      "Scruffy": ["Rufus", "T-Bone"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer

def test_will_return_true_for_a_graph_which_can_be_bipartitioned():
    # Arrange
    dislikes = {
      "Fido": ["Alfie", "Bruno"],
      "Rufus": ["James", "Scruffy"],
      "James": ["Rufus", "Alfie"],
      "Alfie": ["Fido", "James"],
      "T-Bone": ["Scruffy"],
      "Scruffy": ["Rufus", "T-Bone"],
      "Bruno": ["Fido"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert answer

def test_will_return_false_for_graph_which_cannot_be_bipartitioned():
    # Arrange
    dislikes = {
      "Fido": ["Alfie", "Bruno"],
      "Rufus": ["James", "Scruffy"],
      "James": ["Rufus", "Alfie"],
      "Alfie": ["Fido", "James", "T-Bone"],
      "T-Bone": ["Alfie", "Scruffy"],
      "Scruffy": ["Rufus", "T-Bone"],
      "Bruno": ["Fido"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer


def test_will_return_true_for_empty_graph():
    assert possible_bipartition({})
  
def test_will_return_false_for_another_graph_which_cannot_be_bipartitioned():
    # Arrange
    dislikes = {
      "Fido": ["Alfie", "Bruno"],
      "Rufus": ["James", "Scruffy"],
      "James": ["Rufus", "Alfie"],
      "Alfie": ["Fido", "James", "T-Bone"],
      "T-Bone": ["Alfie", "Scruffy"],
      "Scruffy": ["Rufus", "T-Bone"],
      "Bruno": ["Fido"],
      "Calico": ["Nala"],
      "Nala": ["Calico"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer

def test_multiple_dogs_at_beginning_dont_dislike_any_others():
  # Arrange
    dislikes = {
      "Fido": [],
      "Rufus": [],
      "James": [],
      "Alfie": ["T-Bone"],
      "T-Bone": ["Alfie", "Scruffy"],
      "Scruffy": ["T-Bone"],
      "Bruno": ["Nala"],
      "Calico": ["Nala"],
      "Nala": ["Bruno", "Calico"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert answer


def test_multiple_dogs_in_middle_dont_dislike_any_others():
    # Arrange
    dislikes = {
      "Fido": ["Alfie"],
      "Rufus": ["James", "Scruffy"],
      "James": ["Rufus", "Alfie"],
      "Alfie": ["Fido", "James"],
      "T-Bone": [],
      "Scruffy": ["Rufus"],
      "Bruno": [],
      "Spot": ["Nala"],
      "Nala": ["Spot"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert answer

def test_will_return_false_for_disconnected_graph_which_cannot_be_bipartitioned():
    # Arrange
    dislikes = {
      "Katie": ["Michiko"],
      "Michiko": ["Katie"],
      "Fido": ["Alfie", "Bruno"],
      "Rufus": ["James", "Scruffy"],
      "James": ["Rufus", "Alfie"],
      "Alfie": ["Fido", "James", "T-Bone"],
      "T-Bone": ["Alfie", "Scruffy"],
      "Scruffy": ["Rufus", "T-Bone"],
      "Bruno": ["Fido"]
    }

    # Act
    answer = possible_bipartition(dislikes)

    # Assert
    assert not answer


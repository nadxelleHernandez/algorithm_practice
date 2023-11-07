from algorithm_practice.arrays_algorithms import eliminateMaximum

def test_eliminate_maximum_monsters_constant_speed_you_win():
    dist = [1,3,4]
    speed = [1,1,1]

    result = eliminateMaximum(dist, speed)

    assert result == 3

def test_eliminate_maximum_monsters_constant_speed_you_lose():
    dist = [1,1,2,3]
    speed = [1,1,1,1]

    result = eliminateMaximum(dist, speed)

    assert result == 1

def test_eliminate_maximum_monsters_variable_speed_you_lose():
    dist = [3,2,4]
    speed = [5,3,2]

    result = eliminateMaximum(dist, speed)

    assert result == 1

def test_eliminate_maximum_monsters_variable_speed_you_lose_faster_monster_not_at_the_beginning():
    dist = [4,3,4]
    speed = [1,1,2]

    result = eliminateMaximum(dist, speed)

    assert result == 3

def test_eliminate_maximum_monsters_variable_speed_you_lose_faster_same_distance_monsters():
    dist = [5,4,3,3,3]
    speed = [1,1,5,3,1]

    result = eliminateMaximum(dist, speed)

    assert result == 1
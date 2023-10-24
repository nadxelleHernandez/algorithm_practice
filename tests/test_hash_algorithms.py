from algorithm_practice.hash_tables.hash_algorithms import server_failures

def test_server_failures_with_one_failure():
    logs = ["s1 started", "s2 started", "s1 timeout", "s1 failed", "s1 started", "s2 timeout", "s2 failed", "s1 failed", "s1 started", "s1 failed", "s1 failed"]

    assert server_failures(logs) == 1

def test_server_failures_with_same_Server_failing_twice():
    logs = ["s1 started", "s2 started", "s1 timeout", "s1 failed", "s1 started", "s2 timeout", "s1 failed", "s1 failed", "s1 started", "s1 failed", "s1 failed", "s1 failed"]

    assert server_failures(logs) == 2
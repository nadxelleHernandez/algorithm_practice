from algorithm_practice.stacks_queues import Stack, Queue, Queue_O

def test_queue_adding_10_elements():
    queue = Queue()
    queue_0 = Queue_O()
    elem = [1,2,3,4,5,6,7,8,9,10]

    for el in elem:
        queue.enqueue(el)
        queue_0.enqueue(el)

    result = []
    result_o = []
    value = queue.dequeue()
    value_o = queue_0.dequeue()
    while value and value_o:
        result.append(value)
        result_o.append(value_o)
        value = queue.dequeue()
        value_o = queue_0.dequeue()

    assert result == elem
    assert result_o == elem

def test_queue_adding_and_removing_alternating():
    queue = Queue()
    elem = [1,2,3,4,5,6,7,8,9]

    for i in range(5):
        queue.enqueue(elem[i])

    for i in range(4,len(elem)):
        queue.dequeue()
        queue.enqueue(elem[i])

    result = []
    value = queue.dequeue()
    while value:
        result.append(value)
        value = queue.dequeue()

    assert result == [5,6,7,8,9]

def test_queue_o_adding_and_removing_alternating():
    queue = Queue_O()
    elem = [1,2,3,4,5,6,7,8,9]

    for i in range(5):
        queue.enqueue(elem[i])

    for i in range(4,len(elem)):
        queue.dequeue()
        queue.enqueue(elem[i])

    result = []
    value = queue.dequeue()
    while value:
        result.append(value)
        value = queue.dequeue()

    assert result == [5,6,7,8,9]



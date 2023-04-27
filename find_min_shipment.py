def build_min_shipments_dict(l: list[int]) -> dict[int, int]:
    '''
        Input: list of shipment weights
        Output: a dict[weight, freq] 
    '''
    weights = {}
    for e in l:
        if weights.get(e, None) is None:
            weights[e] = 1
        else:
            weights[e] += 1
    return weights

def get_min_shimpments(freq: int) -> int:
    '''
        Returns the number of shipments based to freq of same weighhts
    '''
    return freq//3 + (freq % 3 != 0) if freq > 1 else -1

def find_min_shipments(l: list) -> int:
    weights = build_min_shipments_dict(l)
    sum = 0
    for v in weights.values():
        mins = get_min_shimpments(v)
        if mins == -1:
            return -1
        else:
            sum += mins
    return sum


# unit tests
def test_get_min_shimpments():
    assert get_min_shimpments(1) == -1
    assert get_min_shimpments(2) == 1
    assert get_min_shimpments(3) == 1
    assert get_min_shimpments(4) == 2
    assert get_min_shimpments(5) == 2
    assert get_min_shimpments(6) == 2
    assert get_min_shimpments(7) == 3
    assert get_min_shimpments(8) == 3
    assert get_min_shimpments(9) == 3

def test_find_min_shipments():
    assert find_min_shipments([1,3,2,1,2,1,1]) == -1
    assert find_min_shipments([1,3,2,1,2,1,1,9,3,9,9]) == 5

def run_unit_tests():
    print('test started')
    test_get_min_shimpments()
    test_find_min_shipments()
    print('test completed successfully')

if __name__ == '__main__':
    run_unit_tests()    


from pathfinder import elevation_list

def test_determine_smallest_number():
    options = [432, 842, 123, 764, 763]
    assert max(options) == 842

def test_determine_color_intensity():
    color_intensity = round(4326/5648 * 255)
    assert color_intensity == 195

def test_what_does_enumerate_do():
    x = [432, 764]
    y = enumerate(x)
    assert list(y) == [(0, 432), (1, 764)]

# def test_loop_list_for_color_intensity():
#     collection = [9, 8, 7, 6]
#     item = collection[3]
#     highest_elevation = 10
#     color_formula = round(item / highest_elevation * 255)
#     color_intensity = [color_formula(item) for item in collection]
#     assert color_intensity == 153

def test_does_this_enumerate_lists():
    list_a = [12, 32, 56]
    assert list(enumerate(list_a)) == [(0, 12), (1, 32), (2, 56)]


# def test_value_of_next_step_option():
#     current_step = (elevation_list[2][6])
#     x = current_step[1] +1
#     y = current_step[2] -1
#     step_up = (current_step[x+1][y-1])
#     assert step_up == (current_step[3][5])

def test_can_i_add_to_empty_dict():
    x = 2
    y = 0
    my_dict = {}
    my_dict['new_thing'] = [3, 4]
    assert my_dict == {'new_thing' : [3, 4]}

def test_get_value_of_index_in_dict():
    my_dict = {'up' : (3, 5),
    'down' : (6, 8),
    'fwd' : (1, 0)}
    assert my_dict['fwd'] == (1, 0)
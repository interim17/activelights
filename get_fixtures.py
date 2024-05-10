# Assuming you have a SOP named 'merge_fixtures' in your network
sop = op('merge_fixtures')

universe_table = op('universe_table')
universe_table.clear()
start_stop_table = op('startstoptable')
start_stop_table.clear()
parent_op = op('../..') 
config_table = parent_op.op('LEDMX_port_indices') 
print(config_table)
config_table.clear()
# Initialize universe count and offset
current_universe = 0
offset = 0
# Loop through fixtures
for fixture in sop.inputs:
    start_stop_table.appendRow(current_universe+1)
    config_table.appendRow(current_universe+1)
    # rest point count
    num_points_in_fixture = 0
    # Count points in fixture
    for prim in fixture.prims:
        num_points_in_fixture += len(prim)*3
    while num_points_in_fixture > 510:
        num_points_in_fixture -= 510
        universe_table.appendRow([current_universe, offset])
        current_universe += 1
        offset += 510
    universe_table.appendRow([current_universe, offset])
    current_universe += 1
    offset += num_points_in_fixture
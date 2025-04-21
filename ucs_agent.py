from utilities import get_min, compute_cost
from puzzle8_game import Puzzle8


def ucs(initial_state, get_actions, get_state, is_goal):
    fringe, visited = [], set()

    initial_node = {
        'state': tuple(initial_state),
        'path': [],
        'cost': 0
    }

   
    fringe.append(initial_node)

    while fringe:
        current_node = fringe.pop(get_min(fringe, 'cost'))

        if current_node['state'] in visited:
            continue

        visited.add(current_node['state'])
        
        # Uncomment to debug:
        # print("Exploring:", current_node)

        if is_goal(current_node['state']):
            return {
                'path': current_node['path'],
                'cost': current_node['cost'],
                'expanded_nodes': len(visited)
            }

        possible_actions = get_actions(current_node['state'])

        for action in possible_actions:
            next_state = get_state(action, list(current_node['state']))
            next_node = {
                'state': tuple(next_state),
                'path': current_node['path'] + [action],
                'cost': current_node['cost'] + compute_cost(current_node['state'], action)
            }

            fringe.append(next_node)

    return -1
def main():
   
    puzzle = Puzzle8()
    
    try:
        puzzle.shuffle(10)
    except ValueError as e:
        print(f"Shuffle failed: {e}")
        return

    print("Initial State:")
    puzzle.print_state(puzzle.initial_state)

    # Perform UCS to find the solution
    result = ucs(
        initial_state=puzzle.initial_state,
        get_actions=puzzle.get_actions,
        get_state=puzzle.apply_action,
        is_goal=puzzle.is_goal
    )

    if result == -1:
        print("No solution found.")
    else:
        solution, nodes_explored, cost = result['path'], result['expanded_nodes'], result['cost']
        print(f"\nSolution found in {len(solution)} moves after exploring {nodes_explored} nodes.")
        print(f"Total cost: {cost}")
        print(f"Moves: {' '.join(solution)}")


if __name__ == '__main__':
    main()
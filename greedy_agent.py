from utilities import get_min, h1, h2
from puzzle8_game import Puzzle8


def greedy(initial_state, get_actions, get_state, is_goal, heuristic):
    fringe, visited = [], set()

    initial_node = {
        'state': tuple(initial_state),
        'path': [],
        'h': heuristic(initial_state)
    }

    fringe.append(initial_node)

    while len(fringe) > 0:
        current_node = fringe.pop(get_min(fringe, 'h'))

        if tuple(current_node['state']) in visited:
            continue

        visited.add(tuple(current_node['state']))

        # Uncomment to debug:
        # print("Exploring:", current_node)

        if is_goal(current_node['state']):
            return {
                'path': current_node['path'],
                'expanded_nodes': len(visited)
            }

        possible_actions = get_actions(current_node['state'])

        for action in possible_actions:
            new_state = get_state(action, list(current_node['state']))
            next_node = {
                'state': tuple(new_state),
                'path': current_node['path'] + [action],
                'h': heuristic(new_state)
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

    # Perform Greedy Search with heuristic h1 or h2
    result = greedy(
        initial_state=puzzle.initial_state,
        get_actions=puzzle.get_actions,
        get_state=puzzle.apply_action,
        is_goal=puzzle.is_goal,
        heuristic=h1  # or h2 depending on your choice
    )

    if result == -1:
        print("No solution found.")
    else:
        solution, nodes_explored = result['path'], result['expanded_nodes']
        print(f"\nSolution found in {len(solution)} moves after exploring {nodes_explored} nodes.")
        print(f"Moves: {' '.join(solution)}")


if __name__ == '__main__':
    main()

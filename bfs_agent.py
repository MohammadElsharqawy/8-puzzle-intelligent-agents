from collections import deque
from typing import Callable, List, Tuple, Set, Dict, Any
from puzzle8_game import Puzzle8


def bfs(initial_state, get_actions, get_state, is_goal):
    fringe: deque[Dict[str, Any]] = deque()
    visited: Set[Tuple[int, ...]] = set()

    initial_node = {
        'state': tuple(initial_state),
        'path': []
    }

    fringe.append(initial_node)

    while fringe:
        current_node = fringe.popleft()
        current_state = current_node['state']

        if current_state in visited:
            continue

        visited.add(current_state)

        # Uncomment this for debugging:
        # print("Exploring:", current_node)

        if is_goal(list(current_state)):
            return current_node['path'], len(visited)

        for action in get_actions(list(current_state)):
            next_state = get_state(action, list(current_state))
            next_node = {
                'state': tuple(next_state),
                'path': current_node['path'] + [action]
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

    result = bfs(
        initial_state=puzzle.initial_state,
        get_actions=puzzle.get_actions,
        get_state=puzzle.apply_action,
        is_goal=puzzle.is_goal
    )

    if result == -1:
        print("No solution found.")
    else:
        solution, nodes_explored = result
        print(f"\nSolution found in {len(solution)} moves after exploring {nodes_explored} nodes.")
        print(f"Moves: {' '.join(solution)}")


if __name__ == '__main__':
    main()

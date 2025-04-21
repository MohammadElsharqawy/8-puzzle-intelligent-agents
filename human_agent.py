from puzzle8_game import Puzzle8


def human_solver(puzzle: Puzzle8):
    current_state = puzzle.initial_state

    while True:
        puzzle.print_state(current_state)
        available_moves = puzzle.get_actions(current_state)

        print(f"Available moves: {available_moves}")
        selected_move = input("Select a move (^, v, <, >): ").strip()

        if selected_move not in available_moves:
            print("Invalid move. Game Over.")
            return

        current_state = puzzle.apply_action(selected_move, current_state)

        if puzzle.is_goal(current_state):
            puzzle.print_state(current_state)
            print("Congratulations! You've solved the puzzle.")
            return


def main():
    puzzle = Puzzle8()

    try:
        puzzle.shuffle(N=10)
    except ValueError as e:
        print(f"Shuffle failed: {e}")
        return

    human_solver(puzzle)


if __name__ == '__main__':
    main()

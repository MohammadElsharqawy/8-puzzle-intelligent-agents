import random

class Puzzle8:
    def __init__(self, puzzle=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
        self.initial_state = puzzle

    def print_state(self, puzzle):
        print(
            '-' * 13 + '\n' +
            f'| {puzzle[0]} | {puzzle[1]} | {puzzle[2]} |\n' +
            '-' * 13 + '\n' +
            f'| {puzzle[3]} | {puzzle[4]} | {puzzle[5]} |\n' +
            '-' * 13 + '\n' +
            f'| {puzzle[6]} | {puzzle[7]} | {puzzle[8]} |\n' +
            '-' * 13
        )

    def _get_index_empty_cell(self, puzzle):
        return puzzle.index(0)

    def get_actions(self, puzzle):
        empty = self._get_index_empty_cell(puzzle)
        available_actions = []

        if empty not in [0, 1, 2]:  
            available_actions.append('^')
        if empty not in [6, 7, 8]:  
            available_actions.append('v')
        if empty not in [2, 5, 8]:  
            available_actions.append('>')
        if empty not in [0, 3, 6]: 
            available_actions.append('<')

        return available_actions

    def apply_action(self, selected_move, puzzle):
        empty = self._get_index_empty_cell(puzzle)
        new_state = puzzle[:]

        if selected_move == '>':
            new_state[empty], new_state[empty + 1] = new_state[empty + 1], new_state[empty]
        elif selected_move == '<':
            new_state[empty], new_state[empty - 1] = new_state[empty - 1], new_state[empty]
        elif selected_move == '^':
            new_state[empty], new_state[empty - 3] = new_state[empty - 3], new_state[empty]
        elif selected_move == 'v':
            new_state[empty], new_state[empty + 3] = new_state[empty + 3], new_state[empty]

        return new_state

    def is_goal(self, puzzle):
        return all(i == val for i, val in enumerate(puzzle))

    def count_inversions(self, puzzle):
        inversions = 0
        tiles = [tile for tile in puzzle if tile != 0]

        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if tiles[i] > tiles[j]:
                    inversions += 1

        return inversions

    def is_solvable(self, puzzle):
        return self.count_inversions(puzzle) % 2 == 0

    def shuffle(self, N):
        while True:
            for _ in range(N):
                actions = self.get_actions(self.initial_state)
                self.initial_state = self.apply_action(random.choice(actions), self.initial_state)

            if self.is_solvable(self.initial_state):
                break

        if self.is_goal(self.initial_state):
            raise ValueError("The puzzle is already in the goal state!")

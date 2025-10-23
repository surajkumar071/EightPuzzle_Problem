
v. b. cc. k. VT. jk. ccc. jk.  BBB.



class EightPuzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def display_state(self, state):
        # returns a string representation row-wise
        rows = []
        for i in range(0, 9, 3):
            rows.append(" ".join(str(x) for x in state[i:i+3]))
        return "\n".join(rows)

    def find_zero(self, state):
        return state.index(0)

    def swap(self, state, i, j):
        new_state = state[:]
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    def get_possible_moves(self, state):
        zero_index = self.find_zero(state)
        moves = []
        # Move up
        if zero_index not in [0, 1, 2]:
            moves.append(("Up", self.swap(state, zero_index, zero_index - 3)))
        # Move down
        if zero_index not in [6, 7, 8]:
            moves.append(("Down", self.swap(state, zero_index, zero_index + 3)))
        # Move left
        if zero_index not in [0, 3, 6]:
            moves.append(("Left", self.swap(state, zero_index, zero_index - 1)))
        # Move right
        if zero_index not in [2, 5, 8]:
            moves.append(("Right", self.swap(state, zero_index, zero_index + 1)))
        return moves

    def solve(self):
        # BFS that also tracks the move names
        from collections import deque
        visited = set()
        queue = deque([(self.initial_state, [], [])])  # state, path_states, path_moves
        while queue:
            current_state, path_states, path_moves = queue.popleft()
            if current_state == self.goal_state:
                return path_states + [current_state], path_moves
            t = tuple(current_state)
            if t in visited:
                continue
            visited.add(t)
            for move_name, next_state in self.get_possible_moves(current_state):
                queue.append((next_state, path_states + [current_state], path_moves + [move_name]))
        return None, None

# Example run
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
puzzle = EightPuzzle(initial_state)

print("Initial State (row-wise):")
print(puzzle.display_state(puzzle.initial_state))
print()

print("Possible Moves from Initial State (with directions):")
for move_name, state in puzzle.get_possible_moves(puzzle.initial_state):
    print(f"Move: {move_name}")
    print(puzzle.display_state(state))
    print()

states, moves = puzzle.solve()
if states:
    print("Step-by-step solution:")
    for i, state in enumerate(states):
        if i == 0:
            print(f"Step {i}: Start")
            print(puzzle.display_state(state))
            print()
        else:
            print(f"Step {i}: {moves[i-1]}")
            print(puzzle.display_state(state))
            print()
else:
    print("No solution found.")

from collections import deque


def is_valid(m, c):
    # Number of missionaries and cannibals on the left bank
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False

    # Remaining people on the right bank
    right_m = 3 - m
    right_c = 3 - c

    # Cannibals must not outnumber missionaries
    # wherever missionaries are present
    if m > 0 and c > m:
        return False

    if right_m > 0 and right_c > right_m:
        return False

    return True


def solve():
    # State: (missionaries_left, cannibals_left, boat_side)
    # Boat side: 0 = left, 1 = right
    start = (3, 3, 0)
    goal = (0, 0, 1)

    # The boat can carry one or two people
    passengers = [(1, 0), (2, 0), (0, 1),
                  (0, 2), (1, 1)]

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if (m, c) == (0, 0):
            print("\nSolution found!")
            print("Step 0: Initial state (M_left, C_left, Boat):",
                  start)

            for step, (new_state, action) in enumerate(path, 1):
                print(f"Step {step}: {action} -> {new_state}")

            print("\nAll missionaries and cannibals crossed safely.")
            print("Total crossings:", len(path))
            return

        for pm, pc in passengers:
            if boat == 0:
                new_state = (m - pm, c - pc, 1)
                direction = "Left -> Right"
            else:
                new_state = (m + pm, c + pc, 0)
                direction = "Right -> Left"

            nm, nc, _ = new_state

            if not is_valid(nm, nc):
                continue

            # The boat cannot carry more people than available
            if boat == 0 and (pm > m or pc > c):
                continue

            if boat == 1 and (pm > 3 - m or pc > 3 - c):
                continue

            if new_state not in visited:
                visited.add(new_state)
                action = (
                    f"Move {pm} missionary/missionaries "
                    f"and {pc} cannibal(s), {direction}"
                )
                queue.append(
                    (new_state, path + [(new_state, action)])
                )

    print("No solution found.")


if __name__ == "__main__":
    solve()
from collections import deque
from math import gcd


def water_jug(cap1, cap2, target):
    if target < 0 or target > max(cap1, cap2):
        print("Target cannot be measured.")
        return

    if target != 0 and target % gcd(cap1, cap2) != 0:
        print("Target cannot be measured with these jugs.")
        return

    start = (0, 0)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            print("\nStep 0: Initial state:", start)

            for i, (state, action) in enumerate(path, 1):
                print(f"Step {i}: {action} -> {state}")

            print("\nFinal state:", (a, b))
            print("Total operations:", len(path))
            return

        p12 = min(a, cap2 - b)
        p21 = min(b, cap1 - a)

        moves = [
            ((cap1, b), "Fill Jug 1"),
            ((a, cap2), "Fill Jug 2"),
            ((0, b), "Empty Jug 1"),
            ((a, 0), "Empty Jug 2"),
            ((a - p12, b + p12), "Pour Jug 1 into Jug 2"),
            ((a + p21, b - p21), "Pour Jug 2 into Jug 1")
        ]

        for next_state, action in moves:
            if next_state not in visited:
                visited.add(next_state)
                queue.append(
                    (next_state, path + [(next_state, action)])
                )

    print("No solution found.")


try:
    cap1 = int(input("Enter capacity of Jug 1: "))
    cap2 = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter target quantity: "))

    if cap1 <= 0 or cap2 <= 0:
        print("Capacities must be positive.")
    else:
        water_jug(cap1, cap2, target)

except ValueError:
    print("Please enter valid integers.")
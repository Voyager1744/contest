from collections import defaultdict

def distance_squared(p1, p2):
    """Calculates the squared distance between two points."""
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def is_orthogonal(v1, v2):
    """Checks if two vectors are orthogonal (dot product is zero)."""
    return v1[0] * v2[0] + v1[1] * v2[1] == 0

def find_potential_squares(points):
    """Finds potential positions for completing squares."""
    potential_positions = defaultdict(int)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]
            dist_squared = distance_squared(p1, p2)

            # Calculate potential positions for the other two points
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            for sign1 in [-1, 1]:
                for sign2 in [-1, 1]:
                    new_x, new_y = p1[0] + sign1 * dy, p1[1] - sign1 * dx
                    potential_positions[(new_x, new_y)] += 1

                    new_x, new_y = p2[0] + sign2 * dy, p2[1] - sign2 * dx
                    potential_positions[(new_x, new_y)] += 1

    return potential_positions

def add_points_to_form_square(points):
    """Adds points to the set until a square is formed."""
    added_points = []
    while True:
        potential_positions = find_potential_squares(points + added_points)

        # Find the most frequent potential position
        best_position, max_count = None, 0
        for position, count in potential_positions.items():
            if count > max_count:
                best_position, max_count = position, count

        # If no potential position is found, it's not possible to form a square
        if best_position is None:
            return None

        # Add the best position to the set
        added_points.append(best_position)

        # Check if a square is formed after adding the point
        if find_potential_squares(points + added_points):
            return added_points

# Example usage:
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points = [(1, 2), (3, 4), (5, 6)]
added_points = add_points_to_form_square(points)

if added_points is not None:
    print("Minimum points added:", len(added_points))
    print("Added points:", *added_points)
else:
    print("It's not possible to form a square.")
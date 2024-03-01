def post_correspondence_problem(tiles):
    def dfs(sequence):
        if sequence and sequence[-1][0] == sequence[-1][1]:
            return sequence  # Solution found

        for tile in tiles:
            new_sequence = sequence + tile
            if dfs(new_sequence):
                return new_sequence  # Solution found

        return None  # No solution found

    initial_sequence = []
    solution = dfs(initial_sequence)

    return solution

# Example usage:
tiles = [("01", "0"), ("1", "10"), ("00", "1")]
solution = post_correspondence_problem(tiles)

if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")

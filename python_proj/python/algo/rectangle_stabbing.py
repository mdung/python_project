def rectangle_stabbing(rectangles):
    events = []  # List to store events (start or end of a rectangle)
    for rect in rectangles:
        events.append((rect[0], 'start', rect))
        events.append((rect[2], 'end', rect))

    events.sort()  # Sort events based on x-coordinate

    active_rectangles = set()
    max_stab_count = 0
    max_stab_position = None

    for event in events:
        position, event_type, rect = event

        if event_type == 'start':
            active_rectangles.add(rect)
        else:
            active_rectangles.remove(rect)

        stab_count = len(active_rectangles)

        if stab_count > max_stab_count:
            max_stab_count = stab_count
            max_stab_position = position

    return max_stab_count, max_stab_position

# Example usage:
rectangles = [(1, 1, 4, 4), (2, 2, 5, 5), (3, 3, 6, 6), (7, 1, 9, 4)]
result_count, result_position = rectangle_stabbing(rectangles)

print("Maximum number of rectangles stabbed:", result_count)
print("Stabbing position:", result_position)

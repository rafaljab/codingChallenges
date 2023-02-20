def vacuum_cleaner_route(moves_sequence: str):
    horizontally = 0
    vertically = 0
    for move in moves_sequence:
        if move == 'L':
            horizontally -= 1
        if move == 'R':
            horizontally += 1
        if move == 'U':
            vertically += 1
        if move == 'D':
            vertically -= 1
    return horizontally == 0 and vertically == 0

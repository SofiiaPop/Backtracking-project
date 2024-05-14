"""module for finding words"""
def find_word(grid, word):
    """
    Function finds word
    """
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 0)]
    def backtrack(i, j, idx, direction):
        if idx == len(word):
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return False
        if grid[i][j] == word[idx]:
            next_i, next_j = i + direction[0], j + direction[1]
            return backtrack(next_i, next_j, idx + 1, direction)
        return False
    found = []
    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                if backtrack(i, j, 0, direction) \
and word == ''.join([grid[i+l*direction[0]][j+l*direction[1]] for l in range(len(word))]):
                    found.append((f'Слово "{word}" знайдено в рядку {i} \
стовпці {j}.', direction, i, j))
    return found if found else f'Слово "{word}" не знайдено.'

def result_solve(crossword, words_to_find) -> None:
    """
    Function gives word to find
    """
    for word in words_to_find:
        results = find_word(crossword, word)
        if isinstance(results, list):
            for result in results:
                print(result[0])
        else:
            print(results)

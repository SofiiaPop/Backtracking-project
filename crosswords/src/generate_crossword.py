import random

def can_place_word(crossword_grid, word, row, col, direction):
    if direction == 'horizontal':
        # Перевірка чи може слово поміститися горизонтально
        if col + len(word) > len(crossword_grid):
            return False
        for i in range(len(word)):
            if crossword_grid[row][col+i] != ' ' and crossword_grid[row][col+i] != word[i]:
                return False
    elif direction == 'vertical':
        # Перевірка чи може слово поміститися вертикально
        if row + len(word) > len(crossword_grid):
            return False
        for i in range(len(word)):
            if crossword_grid[row+i][col] != ' ' and crossword_grid[row+i][col] != word[i]:
                return False
    return True

def place_word(crossword_grid, word, row, col, direction):
    if direction == 'horizontal':
        for i in range(len(word)):
            crossword_grid[row][col+i] = word[i]
    elif direction == 'vertical':
        for i in range(len(word)):
            crossword_grid[row+i][col] = word[i]

def generate_crossword(words):
    random.shuffle(words)
    max_length = max(len(word) for word in words)
    crossword_size = max_length * 2
    crossword_grid = [[' ' for _ in range(crossword_size)] for _ in range(crossword_size)]
    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            inserted = False
            while not inserted:
                row = random.randint(0, crossword_size - 1)
                col = random.randint(0, crossword_size - len(word))
                if can_place_word(crossword_grid, word, row, col, direction):
                    place_word(crossword_grid, word, row, col, direction)
                    inserted = True
        elif direction == 'vertical':
            inserted = False
            while not inserted:
                row = random.randint(0, crossword_size - len(word))
                col = random.randint(0, crossword_size - 1)
                if can_place_word(crossword_grid, word, row, col, direction):
                    place_word(crossword_grid, word, row, col, direction)
                    inserted = True
    for row in crossword_grid:
        print(' '.join(row))
    return [[j if j != ' ' else random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')for j in i]\
for i in crossword_grid], words

#_______________________________
# words = [i.upper() for i in ['python', 'crossword', 'generator', 'word', 'grid', 'puzzle']]
# print(generate_crossword(words), words)

def main(number, path_to_file = 'src/dicts/default.txt'):
    """result"""
    with open(path_to_file, 'r', encoding='utf-8') as file:
        words = [i.strip().upper() for i in file.readlines()]
        random.shuffle(words)
        words = words[:number]
    return generate_crossword(words)

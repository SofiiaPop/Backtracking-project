import src.generate_crossword as gen
import src.solve_crossword as sol

def start(number, path_to_file=None):
    """main func"""
    if path_to_file:
        crossword, words = gen.main(number, path_to_file)
    else:
        crossword, words = gen.main(number)
    print('\n#_________________________________________________________________\n')
    for row in crossword:
        print(''.join(row))
    next_line = '\n'
    print(f'Words to find:{next_line}{next_line.join(words)}')
    sol.result_solve(crossword=crossword, words_to_find=words)

start(400)

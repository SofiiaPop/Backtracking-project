# Backtracking

Backtracking - це метод розв'язання задач, який використовується в програмуванні для пошуку рішень у просторі можливих варіантів. Він працює шляхом послідовного спробування різних варіантів рішення, відходячи назад при виявленні, що поточний шлях не веде до рішення. Це особливо корисно у задачах, де потрібно знайти всі можливі рішення або знайти рішення, які задовольняють певні критерії, наприклад, пошук шляхів у графі або генерація всіх перестановок або комбінацій.
Однак, backtracking може бути неефективним, оскільки він може вимагати великої кількості повторних розрахунків, особливо для великих просторів пошуку. Для покращення ефективності використовуються різні техніки, такі як обмеження пошуку, використання хеш-таблиц для збереження вже перевірених станів та застосування алгоритмів, які мінімізують кількість необхідних кроків.

## Судоку
Програма для вирішення Судоку використовує бібліотеку Pygame для візуалізації процесу вирішення. Код структуровано навколо класу Solver, який відповідає за логіку вирішення Судоку та візуалізацію процесу.

### Основні компоненти

•	Клас Sudoku ініціалізує Pygame та встановлює розміри екрану та сітки Судоку відповідно до висоти екрану.
•	Метод draw_grid створює візуальне представлення сетки Судоку на екрані.
•	Метод draw_numbers відображає числа на сітці Судоку, використовуючи Pygame для рендерингу тексту.
•	Перевірка сітки: Метоl check_board перевіряє, чи можна помістити число в конкретну клітинку на сетці Судоку, дотримуючись правил Судоку. Також є метод check_start_board, який перевіряє початкову сітку на правильність входу.
•	Комплексне вирішення: Метод complete завершує сітку Судоку, використовуючи backtracking.
•	Вирішення Судоку: Метод solve викликає процес вирішення, відображаючи кожен крок на екрані та зберігаючи кінцевий результат як зображення.
### Вхідні дані

Програма приймає вхідний файл з розкладкою Судоку або генерує випадкову розкладку. Файл повинен містити 9 рядків, кожен з яких містить 9 цифр від 0 до 9, представляючи собою сітку Судоку.

### Виведення
Кінцевий результат вирішення Судоку зберігається як зображення "sudoku_grid.png" (після закриття вікна pygame). В процесі вирішення кожен крок відображається на екрані.
### Виконання
Програма може бути запущена з вхідним файлом або без нього, коли вона автоматично генерує випадкову розкладку Судоку. Використання аргументe –input_file дозволяє вказати файл з розкладкою Судоку.


## Лабіринт

## Кросворд

## M-covering

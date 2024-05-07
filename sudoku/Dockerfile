FROM python:3.12 as builder
RUN pip install pygame
RUN pip install py-sudoku
COPY . .
ENTRYPOINT ["python", "sudoku_visualisation.py"]
from __future__ import annotations
from more_itertools import batched
from enum import Enum, auto
from typing import List, Tuple, Self
from collections import deque

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

def validate_board(method: Puzzle) -> None:
    def wrapper(self, board: List[List[int]]) -> None:
        if not is_valid_board(board):
            raise ValueError("El tablero no es válido")
        
        if not there_is_empty_space(board):
            raise ValueError("No hay espacio en blanco")

        if not check_solvable(board):
            raise Exception("El puzzle no tiene solución")
            
        return method(self, board)
    return wrapper

def is_valid_board(board: List[List[int]]) -> bool:
    union = sum(board, [])
    return len(board)  == len(union) / len(board) == len(set(union)) / len(board)

def there_is_empty_space(board: List[List[int]]) -> bool:
    return 0 in set(sum(board, []))

def check_solvable(board: List[List[int]]) -> bool:
    size = len(board)
    union = sum(board, [])
    inversions = 0

    for i in range(size * size - 1):
        for j in range(i + 1, size * size):
            if union[i] != 0 and union[j] != 0 and union[i] > union[j]:
                inversions += 1
    
    if size % 2 == 1:
        return inversions % 2 == 0
    else:
        empty_tile_row = size - (union.index(0) // size)
        empty_tile_row_parity = empty_tile_row % 2
        inversions_parity = inversions % 2
        return (empty_tile_row_parity != inversions_parity)

class SlidePuzzle(object):
    @validate_board
    def __init__(self, board: List[List[int]]) -> None:
        self.board = board   

    def find_empty_space_in_board(self) -> Tuple[int]:
        for row, values in enumerate(self.board):
            if 0 not in values:
                continue
            
            for column in range(len(values)):
                if 0 == values[column]:
                    return row, column
    
    def is_solved(self) -> List[List[int]]:
        return SlidePuzzle([list(i) for i in batched(sorted(sum(self.board, []))[1:] + [0], len(self.board))])

    def move_piece(self, direction: Direction) -> None:
        empty_row, empty_col = self.find_empty_space_in_board()

        if direction == Direction.UP and empty_row > 0:
            self.board[empty_row][empty_col], self.board[empty_row - 1][empty_col] = self.board[empty_row - 1][empty_col], self.board[empty_row][empty_col]
        elif direction == Direction.DOWN and empty_row < len(self.board) -1:
            self.board[empty_row][empty_col], self.board[empty_row + 1][empty_col] = self.board[empty_row + 1][empty_col], self.board[empty_row][empty_col] 
        elif direction == Direction.LEFT and empty_col > 0:
            self.board[empty_row][empty_col], self.board[empty_row][empty_col - 1] = self.board[empty_row][empty_col - 1], self.board[empty_row][empty_col] 
        elif direction == Direction.RIGHT and empty_col < len(self.board) -1:
            self.board[empty_row][empty_col], self.board[empty_row][empty_col + 1] = self.board[empty_row][empty_col + 1], self.board[empty_row][empty_col]
    
    def copy(self) -> Self:
        return SlidePuzzle([row[:] for row in self.board])

    def __eq__(self, other: Self) -> bool:
        return self.board == other.board
        
    def __str__(self) -> str:
        return f"{self.board}"

def BFS(puzzle: SlidePuzzle) -> List[Direction]:
    visited_vertices = set()
    queue = deque([(puzzle, [])])
   
    while queue:
        curr_puzzle, path = queue.popleft()
        
        if curr_puzzle == puzzle.is_solved():
            if path != []:
                return path
            return "Ya estaba resuelto"

        visited_vertices.add(tuple(map(tuple, curr_puzzle.board)))
        
        for direction in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
            new_puzzle = curr_puzzle.copy()
            new_puzzle.move_piece(direction)

            if tuple(map(tuple, new_puzzle.board)) not in visited_vertices:
                queue.append((new_puzzle, path + [direction]))


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end = " ")
        print()

def main():
    puzzle = SlidePuzzle([[2, 1, 3], [7, 0, 8], [4, 6, 5]])

    return BFS(puzzle), puzzle

if __name__ ==  "__main__":
    movements, puzzle = main()
    print("Original puzzle")
    print_matrix(puzzle.board)
    print(" ")
    for mov in movements:
        puzzle.move_piece(mov) 
        print(mov)  
        print_matrix(puzzle.board)
        print(" ")
        
    


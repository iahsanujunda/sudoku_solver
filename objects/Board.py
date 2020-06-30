class Board:
    """
    Represents sudoku board

    ...

    Attributes
    ----------
    puzzle : str
        a string to represent sudoku puzzle, must be 81 characters.

    Methods
    -------
    display_board(values=dist)
        Prints the animals name and what sound it makes
    """
    def __init__(self, puzzle):
        assert len(puzzle) == 81, ValueError("Puzzle must be 81 char length")

        self.puzzle = puzzle
        self._rows = 'ABCDEFGHI'
        self._cols = '123456789'
        self._boxes = [r + c for r in self._rows for c in self._cols]

    def _get_puzzle_dict(self) -> dict:
        """

        Returns
        -------
            sudoku_dict: dict
                Sudoku board in dict form
        """
        sudoku_dict = {}
        for val, key in zip(self.puzzle, self._boxes):
            if val == '.':
                sudoku_dict[key] = '123456789'
            else:
                sudoku_dict[key] = val
        return sudoku_dict

    def display_board(self) -> None:
        """
        Display the values as a 2-D grid.

        Parameters
        ----------
            values: dict
                The sudoku in dictionary form
        """
        values = self._get_puzzle_dict()
        width = 1 + max(len(values[s]) for s in self._boxes)
        line = '+'.join(['-' * (width * 3)] * 3)
        for r in self._rows:
            print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                          for c in self._cols))
            if r in 'CF':
                print(line)
        print()

    def update_board_with_grid(self, grid: str) -> None:
        assert len(grid) == 81, ValueError("Grid must be 81 char length")
        self.puzzle = grid

    def update_board_with_dict(self, values_dict: dict) -> None:
        res = []
        for r in self._rows:
            for c in self._cols:
                v = values_dict[r + c]
                res.append(v if len(v) == 1 else '.')

        self.puzzle = res

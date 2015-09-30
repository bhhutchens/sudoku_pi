import re

class Sudoku:
  def __init__(self, unsolved_board):
    # creates the sudoku board as two-dimensional list
    self.solution_board = []
    rows = re.findall('.........', unsolved_board)
    print "***********"
    print rows
    print "***********"
    for row_string in rows:
      row_list = []
      for cell in row_string:
        if cell != "-":
          cell = int(cell)
        row_list.append(cell)
      self.solution_board.append(row_list)
    print "***********"
    print self.solution_board
    self.solved = False

  def solve(self):
    while self.solved == False:
      row_index = 0
      for row in self.solution_board:
        column_index = 0
        for cell in row:
          if cell == "-":
            all_known_numbers = self.find_all_numbers(row_index, column_index)
            missing_numbers = self.find_missing_numbers(all_known_numbers)
            if len(missing_numbers) == 1:
              self.solution_board[row_index][column_index] = missing_numbers[0]
              print("here")
              # self.output(self.solution_board)
          if self.check_if_solved() == True:
            break
          column_index += 1
        row_index += 1
        print("now here")
        print self.solution_board

  def check_if_solved(self):
    for row in self.solution_board:
      for cell in row:
        if cell == "-":
          return
    print("solved")
    self.solved = True

  def find_all_numbers(self, row_index, column_index):
    # add the row, cell, and box together
    numbers_in_row = self.find_numbers_in_row(row_index, column_index)
    numbers_in_column = self.find_numbers_in_column(row_index, column_index)
    numbers_in_box = self.find_numbers_in_box(row_index, column_index)
    all_numbers = numbers_in_row + numbers_in_column + numbers_in_box
    return all_numbers

  def find_numbers_in_box(self, row_index, column_index):
    # find all the numbers in the same box
    numbers_in_box = []
    box_row = row_index / 3
    box_column = column_index / 3
    current_row = 0
    for row in self.solution_board:
      current_column = 0
      for cell in row:
        cells_box_row = current_row / 3
        cells_box_column = current_column / 3
        if box_row == cells_box_row and box_column == cells_box_column and cell != "-":
          numbers_in_box.append(cell)
        current_column += 1
      current_row += 1
    return numbers_in_box

  def find_numbers_in_column(self, row_index, column_index):
    # find all the numbers in the same column
    numbers_in_column = []
    current_row = 0
    for row in self.solution_board:
      current_column = 0
      for cell in row:
        if current_column == column_index and cell != "-":
          numbers_in_column.append(cell)
        current_column += 1
      current_row += 1
    return numbers_in_column

  def find_numbers_in_row(self, row_index, column_index):
    # find all the numbers in the same row
    numbers_in_row = []
    for cell in self.solution_board[row_index]:
      if cell != "-" :
        numbers_in_row.append(cell)
    return numbers_in_row

  def find_missing_numbers(self, all_known_numbers):
    missing_numbers = []
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for possible_number in possible_numbers:
      if possible_number not in all_known_numbers:
        missing_numbers.append(possible_number)
    return missing_numbers

  def output(self, solution_board):
    print
    for row in self.solution_board:
      for cell in row:
        print "%s " % cell
    print


sudoku_board = Sudoku("---26-7-168--7--9-19---45--82-1---4---46-29---5---3-28--93---74-4--5--367-3-18---")
print "********out of method"
print sudoku_board.find_all_numbers(1,1)
print sudoku_board.find_missing_numbers(sudoku_board.find_all_numbers(1,1))
print sudoku_board.find_missing_numbers(sudoku_board.find_all_numbers(1,1))[0]
print "********out SOLVING"
sudoku_board.solve()

1 = [255, 0, 0]
2 = [255, 128, 0]
3 = [255, 255, 0]
4 = [0, 255, 0]
5 = [0, 0, 255]
6 = [128, 0 255]
7 = [255, 0, 255]
8 = [255, 0, 128]

sense.set_pixels(sudoku.solution_board)


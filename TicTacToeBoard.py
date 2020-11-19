class TicTacToeBoard:
    def __init__(self):
        self.b = [['-' for _ in range(3)] for _ in range(3)]
        self.winner = False
        self.proccess = True
        self.row = 0
        self.col = 0
        self.k = 0

    def new_game(self):
        self.__init__()

    def get_field(self):
        return self.b

    def check_field(self):
        for i in range(3):
            if self.b[i][0] == self.b[i][1] == self.b[i][2] and self.b[i][2] != '-':
                self.winner = self.b[i][0]
                break
            if self.b[0][i] == self.b[1][i] == self.b[2][i] and self.b[2][i] != '-':
                self.winner = self.b[0][i]
                break
        if self.b[0][0] == self.b[1][1] == self.b[2][2] and self.b[2][2] != '-':
            self.winner = self.b[0][0]
        if self.b[0][2] == self.b[1][1] == self.b[2][0] and self.b[2][2] != '-':
            self.winner = self.b[0][2]

        if self.winner:
            self.proccess = False
            return self.winner
        elif not self.winner:
            count = 0
            for i in self.b:
                for j in i:
                    if '-' != j:
                        count += 1
            if count == 9:
                self.winner = 'D'
                self.proccess = False
                return 'D'
            return None

    def make_move(self, row, col):
        if not self.proccess:
            return "Игра уже завершена"
        if self.b[row - 1][col - 1] == '-':
            self.k += 1
        if self.k % 2 != 0 and self.proccess and self.b[row - 1][col - 1] == '-':
            self.b[row - 1][col - 1] = 'X'
            self.check_field()
            if self.proccess:
                return 'Продолжаем играть'
        elif self.k % 2 == 0 and self.proccess and self.b[row - 1][col - 1] == '-':
            self.b[row - 1][col - 1] = '0'
            self.check_field()
            if self.proccess:
                return 'Продолжаем играть'
        if self.winner == 'D':
            return 'Ничья'
        if self.b[row - 1][col - 1] != '-' and self.proccess:
            return 'Клетка ' + str(row) + ', ' + str(col) + ' уже занята'
        if self.k % 2 != 0 and not self.proccess:
            return 'Победил игрок X'
        elif self.k % 2 == 0 and not self.proccess:
            return 'Победил игрок 0'

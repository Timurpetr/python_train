import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init()

    def show(self):
        for row in self.pole:
            line = []
            for cell in row:
                if not cell.fl_open:
                    line.append("#")
                else:
                    if cell.mine:
                        line.append("*")
                    line.append(cell.around_mines)
            print("".join(line))

    def init(self):
        N = self.N
        M = self.M
        if M > N * N:
            raise ValueError("Слишком много мин для данного поля")

        for i in range(N):
            for j in range(N):
                self.pole[i][j].mine = False
                self.pole[i][j].around_mines = 0
                self.pole[i][j].fl_open = False

        all_cells = [(i, j) for i in range(N) for j in range(N)]
        mine_positions = random.sample(all_cells, M)

        for i, j in mine_positions:
            self.pole[i][j].mine = True
        for i in range(N):
            for j in range(N):
                if self.pole[i][j].mine:
                    continue
                count = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if self.pole[ni][nj].mine:
                                count += 1
                self.pole[i][j].around_mines = count


pole_game = GamePole(10, 12)

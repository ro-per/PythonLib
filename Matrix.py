import random as rand


class Matrix:
    def __init__(self, N=5, random=False):
        self.size = N
        if random:
            self.data = [[rand .randint(0, N*N)
                          for i in range(N)] for j in range(N)]
        else:
            self.data = [[0 for i in range(N)] for j in range(N)]

    def __str__(self):
        s = '\n'
        for i in range(self.size):
            for j in range(self.size):
                s += str(self.data[i][j]) + '\t'
            s += '\n'
        return s

    #TODO Exlcude diagonal
    def iter_triangle(self, tag):
        N = self.size
        print("Iterarting over matrix following {}".format(tag))

        if tag == 'a':
            for r in range(N):
                for c in range(r, N):
                    yield (r, c)
        elif tag == 'b':
            for r in range(N):
                for c in range(r+1):
                    yield (r, c)
        elif tag == 'c':
            for r in range(N):
                for c in range(N-r):
                    yield (r, c)
        elif tag == 'd':
            for r in range(N):
                for c in range(N-r-1, N):
                    yield (r, c)
        else:
            print("Error")

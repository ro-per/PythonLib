class ProgressCounter:
    def __init__(self, n, print_length):
        self.N = n
        self.x = 0
        if print_length > 100:
            print_length = 100
        self.length = print_length
        self.frac = 0
        self.y = 0

    def tick(self, ind):
        self.frac = ind / self.N
        self.y = int(self.frac * self.length)

        if self.y > self.x:
            self.x = self.y
            print(self)

    def __str__(self):
        a = "["
        b = "=" * self.x
        c = " " * (self.length - self.x - 1)
        d = "]"
        percentage = int(self.frac * 100)
        e = " {}%".format(percentage)
        progress = a + b + c + d + e
        return str(progress)

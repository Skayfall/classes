class OddEvenSeparator:
    def __init__(self):
        chet = []
        nechet = []

    def add_number(self, n):
        if n % 2 == 0:
            self.chet.append(n)
        elif n % 2 != 0:
            self.nechet.append(n)

    def even(self):
        return self.chet

    def odd(self):
        return self.nechet

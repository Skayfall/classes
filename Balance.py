class Balance:
    def __init__(self):
        a == 0
        b == 0

    def add_right(self, a):
        self.a = a

    def add_left(self, b):
        self.b = b
        
    def result(self):
        if self.a == self.b:
            return '='
        elif self.a > self.b:
            return 'R'
        else:
            return "L"

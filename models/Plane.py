class Plane:
    def __init__(self, code: str):
        self.code = code
        self.capacity: int = 168
        self.premium_seats: int = 24
        self.economic_seats: int = 144
# track.py 

class Track:
    def __init__(self, num_rows, speed, tempo, name):
        self.name = name
        self.num_rows = num_rows
        self.speed = speed
        self.tempo = tempo

        self.num_cols = 5
        self.eff_cols = []
    
        self.orders = {}
        self.tokens = {}
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "num_rows": self.num_rows,
            "speed": self.speed,
            "tempo": self.tempo,
            "num_cols": self.num_cols,
            "eff_cols": self.eff_cols,
            "orders": self.orders,
            "tokens": self.tokens,
        }

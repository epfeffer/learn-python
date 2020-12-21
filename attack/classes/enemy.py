class Enemy:
    def __init__(self, hp, mp):
        # Health Points (HP)
        self.max_hp = hp
        self.hp = hp
        # Magic Points (MP)
        self.max_mp = mp
        self.mp = mp
    
    
    def get_hp(self):
        return self.hp
    
class Player:
    def __init__(self, name, bod=3, int=3, ref=3, tech=3, cool=3):
        self.name = name
        self.bod = bod
        self.int = int
        self.ref = ref
        self.tech = tech
        self.cool = cool

    def get_name(self):
        return self.name

    def get_body(self):
        return self.bod

    def get_intelligence(self):
        return self.int

    def get_reflexes(self):
        return self.ref

    def get_tech(self):
        return self.tech

    def get_cool(self):
        return self.cool
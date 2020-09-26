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

    def get_all_attr(self):
        return self.bod, self.int, self.ref, self.tech, self.cool

    def change(self, lst):
        if lst[0] == "bod" or lst[0] == "body":
            self.bod += lst[1]
            value = self.bod
        elif lst[0] == "intelligence" or lst[0] == "int":
            self.int += lst[1]
            value = self.int
        elif lst[0] == "reflexes" or lst[0] == "ref":
            self.ref += lst[1]
            value = self.ref
        elif lst[0] == "tech":
            self.tech += lst[1]
            value = self.tech
        elif lst[0] == "cool":
            self.cool += lst[1]
            value = self.cool
        return value

    def see_change(self, lst):
        if lst[0] == "bod" or lst[0] == "body":
            value = self.bod + lst[1]
        elif lst[0] == "intelligence" or lst[0] == "int":
            value = self.int + lst[1]
        elif lst[0] == "reflexes" or lst[0] == "ref":
            value = self.ref + lst[1]
        elif lst[0] == "tech":
            value = self.tech + lst[1]
        elif lst[0] == "cool":
            value = self.cool + lst[1]
        return value
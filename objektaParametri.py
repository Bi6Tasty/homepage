class Square:
    def __init__(self, garums, platums, laukums, hipotenūza):
        self.garums = garums
        self.platums = platums
        self.laukums = laukums
        self.hipotenūza = hipotenūza
    def vertiba(self):
        print(f"garums: {self.garums} cm")
        print(f"platums: {self.platums} cm")
        print(f"laukums: {self.laukums} cm")
        print(f"hipotenūza: {self.hipotenūza} cm")

s1 = Square("10", "50", 10*50, (10**2 + 50**2)**0.5)

s1.vertiba()
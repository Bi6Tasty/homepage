class PC:
    def __init__(self, nos, CPU, HDD, RAM,):
        self.nos = nos
        self.CPU = CPU
        self.HDD = HDD
        self.RAM = RAM

    def display_info(self):
        print(f"PC Name: {self.nos}")
        print(f"CPU: {self.CPU}")
        print(f"HDD: {self.HDD}")
        print(f"RAM: {self.RAM} GB")



pc1 = PC("Desktop_M-11", "ryzen 5", "1TB", "16")

pc1.display_info()

class Car:
    def __init__(self, brand, engine_number):
        self.brand = brand           
        self.__engine_number = engine_number  

    def display_engine_number(self):
        print(f"Engine Number: {self.__engine_number}")

    def __start_the_engine(self):
        print("Engine started.")

    def start_the_car(self):
        self.__start_the_engine()

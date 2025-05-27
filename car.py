class Car:
    def __init__(self, brand, engine_number):
        self.brand = brand                      
        self.__engine_number = engine_number    

    def display_engine_number(self):
        print(f"Engine Number: {self.__engine_number}") 

    def __start_the_engine(self):
        print("Engine started...")  

    def start_the_car(self):
        self.__start_the_engine()   


if __name__ == "__main__":
    car1 = Car("Toyota", "A12345")
    print("Car 1 Brand:", car1.brand)
    car1.display_engine_number()
    car1.start_the_car()

    print()

    car2 = Car("Honda", "B67890")
    print("Car 2 Brand:", car2.brand)
    car2.display_engine_number()
    car2.start_the_car()

    print()


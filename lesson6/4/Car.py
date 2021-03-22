class Car:

    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self) -> None:
        print("The car started!!!")

    def stop(self) -> None:
        print("The car stopped!!!")

    def turn(self, direction: str) -> None:
        print(f"The car turned {direction}")

    def show_speed(self) -> None:
        print(f"Current speed is {self.speed}")


class TownCar(Car):

    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self) -> None:
        if self.speed > 60:
            print("Speed limit exceeded")
        else:
            print(f"Current speed is {self.speed}")


class WorkCar(Car):

    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self) -> None:
        if self.speed > 40:
            print("Speed limit exceeded")
        else:
            print(f"Current speed is {self.speed}")


class PoliceCar(Car):

    def __init__(self, speed: float, color: str, name: str, is_police: bool = True):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):

    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        super().__init__(speed, color, name, is_police)


car1: TownCar = TownCar(39.0, 'Red', 'Car1')
car1.go()
car1.turn("left")
car1.stop()
car1.show_speed()

car2: TownCar = TownCar(61.0, 'Red', 'Car1')
car2.show_speed()

car3: PoliceCar = PoliceCar(61.0, 'Red', 'Car2')
car3.show_speed()

car4: SportCar = SportCar(61.0, 'Red', 'Car3')
car4.go()
car4.show_speed()

car5: WorkCar = WorkCar(61.0, 'Red', 'Car4')
car5.show_speed()

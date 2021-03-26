import time


class TrafficLight:

    def __init__(self):
        self.__color = None

    def running(self) -> None:
        while True:
            self.__switch_lights()

    def __switch_lights(self) -> None:
        self.__color = 'Red'
        print(self.__color)
        time.sleep(7)
        self.__color = 'Yellow'
        print(self.__color)
        time.sleep(5)
        self.__color = 'Green'
        print(self.__color)
        time.sleep(10)


traffic_light: TrafficLight = TrafficLight()
traffic_light.running()

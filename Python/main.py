from car import Car
from account import Account

if __name__ == "__main__":

    car = Car("AMS234", Account("Samuel Zurisaday", "ANDA897"))
    print(vars(car))
    print(vars(car.driver))
    # car = Car()
    # car.license = "AMS1322"
    # car.driver  = "Andrea Rivera"
    # print(vars(car))

    # car2 = Car()
    # car2.license = "JKX2836"
    # car2.driver  = "Samuel Zurisaday"
    # print(vars(car2))

# alternatively, use num_passengers with self._max_passengers = num_passengers but that maeks less sense
class Vehicle():
    def __init__(self, num_seats, num_wheels, max_speed):
        self._max_passengers = num_seats
        self._num_wheels = num_wheels
        self._max_speed = max_speed

class Car(Vehicle):
    def __init__(self, num_seats, max_speed):
        CAR_WHEELS = 4
        Vehicle.__init__(self, num_seats, CAR_WHEELS, max_speed)

class SportsCar(Car):
    def __init__(self, max_speed):
        SPORTS_CAR_SEATS = 2
        SPORTS_CAR_MAX_SPEED = 300
        Car.__init__(self, SPORTS_CAR_SEATS, SPORTS_CAR_MAX_SPEED)

class Bicycle(Vehicle):
    def __init__(self, max_speed):
        BICYCLE_RIDERS = 1
        BICYCLE_WHEELS = 2
        Vehicle.__init__(self, BICYCLE_RIDERS, BICYCLE_WHEELS, max_speed)

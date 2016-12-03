# alternatively, use num_passengers with self._max_passengers = num_passengers but that maeks less sense
class Vehicle():
    def __init__(self, num_seats, num_wheels, max_speed):
        self._max_passengers = num_seats
        self._num_wheels = num_wheels
        self._max_speed = max_speed

class Car(Vehicle):
    CAR_WHEELS = 4

    def __init__(self, num_seats, max_speed):
        Vehicle.__init__(self, num_seats, CAR_WHEELS, max_speed)

class SportsCar(Car):
    SPORTS_CAR_SEATS = 2
    SPORTS_CAR_MAX_SPEED = 300

    def __init__(self, max_speed):
        Car.__init__(self, SPORTS_CAR_SEATS, SPORTS_CAR_MAX_SPEED)

class Bicycle(Vehicle):
    BICYCLE_RIDERS = 1
    BICYCLE_WHEELS = 2

    def __init__(self, max_speed):
        Vehicle.__init__(self, BICYCLE_RIDERS, BICYCLE_WHEELS, max_speed)
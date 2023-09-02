import math
import random


def TimeDuration(distance: float) -> float:
    """
    generates a random time duration in minutes

    returns:
    :float: random time duration in minutes
    """
    # generate a random time duration between 99% and 120% of the distance
    random_time: float = random.uniform((distance * 0.99), (distance * 1.2))
    return random_time


class ObstructionDetector:
    """
    determines if there's an obstruction bewteen points A and B
    if there is an obstruction, determines if it is penetrable or not
    """
    EARTH_RADIUS_MILES: float = 3958.8
    OBSTRUCTION_THRESHOLD_MINUTES: int = 60
    SPEED: float = 1.00  # speed in miles per minute

    def __init__(self, PointA: list[float], PointB: list[float]) -> None:
        """
        initialize instance of ObstructionDetector
        with instance attributes PointA and Point_B

        :param PointA(list[float]): GIS point data for point A
        :param PointB(list[float]): GIS point data for point A
        """
        if isinstance(PointA, list):
            if isinstance(PointA[0], float) and isinstance(PointA[1], float):
                self.PointA: list[float] = PointA
            else:
                raise TypeError("list should contain two floats")
        else:
            raise TypeError("argument must be a list of two floats")

        if isinstance(PointB, list):
            if isinstance(PointB[0], float) and isinstance(PointB[1], float):
                self.PointB: list[float] = PointB
            else:
                raise TypeError("list should contain two floats")
        else:
            raise TypeError("argument must be a list of two floats")
        self. time_from_TimeDuration: float = TimeDuration(
            self.calculate_distance())

    def calculate_distance(self):
        """
        determines the distance between PointA and PointB

        returns:
        :float: the distance between points A and B in miles
        """

        # convert latitude and longitude from degrees to radians
        lat1_rad: float = math.radians(self.PointA[0])
        lon1_rad: float = math.radians(self.PointA[1])
        lat2_rad: float = math.radians(self.PointB[0])
        lon2_rad: float = math.radians(self.PointB[1])

        # get differences between the coordinates
        delta_lat: float = lat2_rad - lat1_rad
        delta_lon: float = lon2_rad - lon1_rad

        # Haversine formula intermediate calculations
        haversine_a: float = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * \
            math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
        haversine_c: float = 2 * math.atan2(math.sqrt(haversine_a),
                                            math.sqrt(1 - haversine_a))

        # calculate distance
        distance: float = self.EARTH_RADIUS_MILES * haversine_c
        return distance

    def calculate_expected_time(self) -> float:
        """
        calculate the expected time to travel from point A to point B based on
            the speed and distance

        : return:    expected time in minutes
        """
        expected_time: float = self.calculate_distance() / self.SPEED
        return expected_time

    def check_obstruction(self) -> bool:
        """
        check for obstructions between points A and B

        : param time_from_TimeDuration: Time calculated from the TimeDuration
            module in minutes

        : return:    True or False
        """
        expected_time: float = self.calculate_expected_time()

        return self.time_from_TimeDuration > expected_time

    def impenetrable(self) -> bool:
        """
        checks if obstructions between points A and B are impenetrable

        : param time_from_TimeDuration: Time calculated from the TimeDuration
            module in minutes

        : return:    True or False
        """
        if self.check_obstruction():
            obstruction_threshold: float = self.calculate_expected_time()
            obstruction_threshold += self.OBSTRUCTION_THRESHOLD_MINUTES
            return self.time_from_TimeDuration >= obstruction_threshold
        else:
            return False

class ObstructionDetector:
    def __init__(self, speed, distance) -> None:
        """
        initialize instance of ObstructionDetector with the speed of the
            machine and the distance between points A and B

        :param speed: Speed of the machine in miles per minute
        :param distance: Distance between points A and B in miles
        """
        self.speed = speed
        self.distance = distance

    def calculate_expected_time(self) -> float:
        """
        calculate the expected time to travel from point A to point B based on
            the speed and distance

        :return:    Expected time in minutes
        """
        expected_time: float = self.distance / self.speed
        return expected_time

    def check_obstruction(self, time_from_TimeDuration) -> bool:
        """
        check for obstructions between points A and B

        :param time_from_TimeDuration: Time calculated from the TimeDuration
            module in minutes

        :return:    True or False
        """
        expected_time: float = self.calculate_expected_time()

        return True if time_from_TimeDuration > expected_time else False

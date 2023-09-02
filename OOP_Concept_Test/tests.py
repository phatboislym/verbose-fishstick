
from obstruction_detector_ZUR000226WSG import ObstructionDetector, TimeDuration
import unittest


class TestObstructionDetector(unittest.TestCase):

    def test_calculate_distance(self):
        # test the calculate_distance method
        point_a: list[float] = [37.7749, -122.4194]  # San Francisco
        point_b: list[float] = [34.0522, -118.2437]  # Los Angeles
        detector: ObstructionDetector = ObstructionDetector(point_a, point_b)

        # the distance between San Francisco and Los Angeles is ~ 347.49 miles
        expected_distance: float = 347.43
        calculated_distance: float = detector.calculate_distance()

        self.assertAlmostEqual(calculated_distance,
                               expected_distance, places=2)

    def test_calculate_expected_time(self):
        # test the calculate_expected_time method
        point_a: list[float] = [37.7749, -122.4194]
        point_b: list[float] = [34.0522, -118.2437]
        detector: ObstructionDetector = ObstructionDetector(point_a, point_b)

        # assuming a speed of 1.00 miles/minute, expected time is 347.49 minutes
        expected_time: float = 347.43
        calculated_time: float = detector.calculate_expected_time()

        self.assertAlmostEqual(calculated_time, expected_time, places=2)

    def test_check_obstruction(self):
        # Test the check_obstruction method with a random time duration
        point_a: list[float] = [37.7749, -122.4194]
        point_b: list[float] = [34.0522, -118.2437]
        detector: ObstructionDetector = ObstructionDetector(point_a, point_b)

        # Assuming a random time duration within 90% - 110% of the expected time
        random_time: float = detector.time_from_TimeDuration
        expected_time: float = detector.calculate_expected_time()

        # The check_obstruction method should return True,
        # as random_time is greater than expected_time
        self.assertTrue(detector.check_obstruction())

    def test_impenetrable(self):
        # test the impenetrable method with an obstruction
        point_a: list[float] = [37.7749, -122.4194]
        point_b: list[float] = [34.0522, -118.2437]
        detector: ObstructionDetector = ObstructionDetector(point_a, point_b)

        # assuming a random time duration within 90% - 110% of the expected time
        random_time: float = detector.time_from_TimeDuration
        expected_time: float = detector.calculate_expected_time()

        # make sure check_obstruction returns True
        self.assertTrue(detector.check_obstruction())

        # the impenetrable method should return False,
        # as random_time is not greater than or equal to the threshold
        self.assertFalse(detector.impenetrable())


if __name__ == '__main__':
    unittest.main(verbosity=2)

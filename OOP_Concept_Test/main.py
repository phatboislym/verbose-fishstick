from obstruction_detector_ZUR000226WSG import ObstructionDetector


def test(pointA, pointB) -> None:
    obstruction_checker = ObstructionDetector(pointA, pointB)
    print(f"distance: {obstruction_checker.calculate_distance():.2f} miles")
    print("time (minutes)")
    print(f"expected: {obstruction_checker.calculate_expected_time():.2f}")
    print(f"elapsed: {obstruction_checker.time_from_TimeDuration:.2f}")

    if obstruction_checker.check_obstruction():
        if obstruction_checker.impenetrable():
            print("impenetrable obstruction")
        else:
            print("penetrable obstruction")
    else:
        print("no obstruction")


def demarcate(num: int = 25) -> None:
    print("-" * num)


if __name__ == '__main__':

    # Example usage
    point_a: list[float] = [37.7749, -122.4194]  # San Francisco
    point_b: list[float] = [34.0522, -118.2437]  # Los Angeles
    point_c: list[float] = [40.7128, -74.0060]  # New York

    test(point_a, point_b)
    demarcate()
    test(pointA=point_b, pointB=point_c)

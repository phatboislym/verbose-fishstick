from obstruction_detector import ObstructionDetector


if __name__ == '__main__':

    # Example usage
    speed_of_machine = 2.5  # miles per minute (simulated)
    distance_ab = 100  # miles (simulated)
    time_from_TimeDuration = 41  # minutes (simulated)

    obstruction_checker = ObstructionDetector(speed_of_machine, distance_ab)
    if obstruction_checker.check_obstruction(time_from_TimeDuration):
        print("obstruction detected")
        if (time_from_TimeDuration >=
                obstruction_checker.calculate_expected_time() + 60):
            print("obstruction is impenetrable")
    else:
        print("no obstruction detected")

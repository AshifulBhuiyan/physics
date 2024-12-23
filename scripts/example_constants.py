from constants.physical_constants import PhysicalConstants

def main():
    print("Speed of Light:", PhysicalConstants.SPEED_OF_LIGHT, "m/s")
    print("All constants:")
    for name, value in PhysicalConstants.get_all_constants().items():
        print(f"{name}: {value}")

if __name__ == "__main__":
    main()

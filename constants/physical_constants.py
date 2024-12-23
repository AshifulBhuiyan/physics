class PhysicalConstants:
    SPEED_OF_LIGHT = 299_792_458  # m/s
    GRAVITATIONAL_CONSTANT = 6.67430e-11  # m^3 kg^-1 s^-2
    PLANCK_CONSTANT = 6.62607015e-34  # Js
    BOLTZMANN_CONSTANT = 1.380649e-23  # J/K

    @staticmethod
    def get_all_constants():
        return {
            "speed_of_light": PhysicalConstants.SPEED_OF_LIGHT,
            "gravitational_constant": PhysicalConstants.GRAVITATIONAL_CONSTANT,
            "planck_constant": PhysicalConstants.PLANCK_CONSTANT,
            "boltzmann_constant": PhysicalConstants.BOLTZMANN_CONSTANT,
        }
"""Docstrings and spacing exercise."""


class OnBoardTemperatureSensor:
    """Temperature sensor class."""

    VOLTAGE_TO_TEMP_FACTOR = 5.6

    def __init__(self):
        """Initialize sensor."""
        pass

    def read_voltage(self):
        """Read voltage."""
        return 2.7

    def get_temperature(self):
        """Get temperature (in celsius)."""
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR


class CarbonMonoxideSensor:
    """Carbon monoxide sensor class."""

    VOLTAGE_TO_CO_FACTOR = 0.048

    def __init__(self, temperature_sensor):
        """Initialize sensor."""
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Get carbon monoxide level."""
        sensor_voltage = self.read_sensor_voltage()
        carbon_monoxide = CarbonMonoxideSensor.convert_voltage_to_carbon_monoxide_level(
            self, sensor_voltage, self.on_board_temp_sensor.get_temperature())
        return carbon_monoxide

    def read_sensor_voltage(self):
        """Read sensor voltage."""
        return 2.3  # In real life, it should read from hardware.

    def convert_voltage_to_carbon_monoxide_level(self, voltage, temperature):
        """Convert voltage to carbon monoxide level."""
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature


class DisplayUnit:
    """Display unit class."""

    def __init__(self):
        """Initialize display unit."""
        self.string = ''

    def display(self, msg):
        """Display message."""
        print(msg)


class CarbonMonoxideDevice():
    """Carbon monoxide device class."""

    def __init__(self, co_sensor, display_unit):
        """Initialize device."""
        self.carbon_monoxide_sensor = co_sensor
        self.display_unit = display_unit

    def display(self):
        """Display carbon monoxide level."""
        msg = 'Carbon Monoxide Level is : ' + \
            str(self.carbon_monoxide_sensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)


if __name__ == '__main__':
    temp_sensor = OnBoardTemperatureSensor()
    sensor = CarbonMonoxideSensor(temp_sensor)
    display = DisplayUnit()
    co_device = CarbonMonoxideDevice(sensor, display)
    co_device.display()

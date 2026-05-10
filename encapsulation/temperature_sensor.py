"""
Exercise 1: TemperatureSensor
Design Temperature Sensor Class
Problem: Build a TemperatureSensor class that collects temperature readings and provides statistical access. 
The sensor should validate that readings fall within a reasonable range and never expose its internal list of readings directly.

Requirements:

Private list of readings
addReading(value): adds a temperature reading, but only if it's between -50 and 150 degrees (inclusive). Reject out-of-range values.
getAverage(): returns the average of all readings, or 0 if no readings exist
getReadingCount(): returns how many readings have been recorded
getReadings(): returns a copy of the readings list (not the original)
"""

class TemperatureSensor:
    def __init__(self):
        self._readings: list[float] = []

    def add_reading(self, value: float) -> None:
        # Only add if value is between -50 and 150 (inclusive)
        if -50 <= value <= 150:
            self._readings.append(value)

    def get_average(self) -> float:
        # Return the average of all readings, or 0.0 if no readings exist
        if len(self._readings) > 0:
            return round(sum(self._readings) / len(self._readings), 2)
        else:
            return 0.0

    def get_reading_count(self) -> int:
        # Return how many readings have been recorded
        return len(self._readings)

    def get_readings(self) -> list[float]:
        # Return a copy of the readings list (not the original)
        return self._readings.copy()
    


if __name__ == "__main__":
    sensor = TemperatureSensor()
    sensor.add_reading(22.5)
    sensor.add_reading(23.1)
    sensor.add_reading(200.0)  # Should be rejected
    sensor.add_reading(-10.0)

    print(f"Count: {sensor.get_reading_count()}")  # 3
    print(f"Average: {sensor.get_average()}")       # 11.87
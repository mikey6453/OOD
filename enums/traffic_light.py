"""
Exercise 1: Traffic Light
Design Traffic Light Class
easy
Problem: Create a TrafficLight enum where each light has a color (RED, YELLOW, GREEN), a 
duration in seconds, and a next() method that returns the next light in the cycle (RED -> GREEN -> YELLOW -> RED).

Requirements:

Each light has a duration property: RED = 30s, YELLOW = 5s, GREEN = 25s
next() method returns the next TrafficLight in the cycle
display() method prints the color and duration
"""

from enum import Enum

class TrafficLight(Enum):
    RED = 30
    YELLOW = 5
    GREEN = 25

    def next(self):
        if self == TrafficLight.RED:
            return TrafficLight.GREEN
        elif self == TrafficLight.GREEN:
            return TrafficLight.YELLOW
        else:
            return TrafficLight.RED
    
    def display(self):
        print(f"{self.name} ({self.value}s)")


if __name__ == "__main__":
    traffic_light = TrafficLight.RED
    print(traffic_light) # TrafficLight.RED

    print(traffic_light.next()) # TrafficLight.GREEN
    traffic_light = traffic_light.next()

    traffic_light.display() # GREEN, 25
    print(traffic_light) # TrafficLight.GREEN

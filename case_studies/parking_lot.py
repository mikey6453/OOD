"""
Parking Lot Case Study

“Imagine you’re arriving at a busy parking lot, eager to park your car. At the entrance, 
you’re issued a ticket. You then drive in, find a spot suited to your vehicle’s size, and park. 
Later, when you prepare to leave, you present your ticket at the exit, the system calculates your fee, 
and the spot is freed up for the next vehicle. Behind the scenes, the parking lot is assigning spots based 
on vehicle size, recording entry and exit times, and updating availability for new arrivals. Now, let’s 
design a parking lot system that handles all this.”

Requirements:
1. the number of spots is configurable at construction - not hardcoded
2. Multi-floor parking garage - different floors can have different amount of spots
3. vehicle sizes - motorcycle, car, truck. smaller vechicles can occuy bigger spots, but not vise versa
4. different types of spots - for motorcycle, car, truck
5. Payment component:
    - vehicle enters
    - recieve ticket with their entry time
    - when they exit, system calculates their fee based on: vehicle type and duration
    - motorcycle: $2/hr, car: $4/hr, truck: $6/hr - payment always succeeds
    - if lot is full, reject payment
"""


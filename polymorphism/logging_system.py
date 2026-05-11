"""
Exercise 2: Logging System
Design Logging System Class
Problem: Build a logging system where the application uses a Logger interface polymorphically. 
Different logger implementations send messages to different destinations, and the application doesn't know or care which one it's using.

Requirements:

Logger interface with log(level, message) and getDestination() methods.
ConsoleLogger: prints formatted log messages to the console.
FileLogger: simulates writing to a file (print with file path prefix).
DatabaseLogger: simulates inserting into a database (print with table name prefix).
Application class that takes a Logger in its constructor and uses it throughout.
"""


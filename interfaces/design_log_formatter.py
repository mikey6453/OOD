"""
Design Log Formatter Class
Problem: Build a logging system where the format of log messages is configurable. A Logger class writes log messages, but the format (plain text vs. JSON) is determined by an injected Formatter interface.

Requirements:

Formatter interface with a format(message) method that takes a string and returns a formatted string
PlainFormatter: returns the message as-is (e.g., "Server started on port 8080")
JsonFormatter: returns the message wrapped in JSON (e.g., {"log": "Server started on port 8080"})
Logger class takes a Formatter in its constructor and has a log(message) method that formats the message, then prints it
"""

from abc import ABC, abstractmethod

class Formatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass


class PlainFormatter(Formatter):
    def format(self, message: str) -> str:
        return message


class JsonFormatter(Formatter):
    # Return the message wrapped in JSON: {"log": "message"}
    def format(self, message: str) -> str:
        return f'{{"log": "{message}"}}'


class Logger:
    def __init__(self, formatter: Formatter):
        self._formatter = formatter


    def log(self, message: str) -> None:
        print(self._formatter.format(message))


if __name__ == "__main__":
    plain_logger = Logger(PlainFormatter())
    plain_logger.log("The server started on port 8080")

    json_logger = Logger(JsonFormatter())
    json_logger.log("The server started on port 8080")
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

from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        pass

    @abstractmethod
    def get_destination(self) -> str:
        pass


class ConsoleLogger(Logger):
    def log(self, level: str, message: str) -> None:
        print(f"[{level}] {message}")

    def get_destination(self) -> str:
        return "Console"


class FileLogger(Logger):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def log(self, level: str, message: str) -> None:
        print(f"Writing to {self._file_path}: [{level}] {message}")

    def get_destination(self) -> str:
        return f"File: {self._file_path}"


class DatabaseLogger(Logger):
    def __init__(self, table_name: str):
        self._table_name = table_name

    def log(self, level: str, message: str) -> None:
        print(f"INSERT INTO {self._table_name}: [{level}] {message}")

    def get_destination(self) -> str:
        return f"Database: {self._table_name}"


class Application:
    def __init__(self, logger: Logger):
        self._logger = logger

    def run(self):
        self._logger.log("INFO", "Application starting...")
        self._logger.log("INFO", "Processing data...")
        self._logger.log("INFO", "Application shutting down.")


if __name__ == "__main__":
    loggers = [
        ConsoleLogger(),
        FileLogger("/var/log/app.log"),
        DatabaseLogger("app_logs"),
    ]

    for logger in loggers:
        print(f"--- Using {logger.get_destination()} ---")

        app = Application(logger)

        app.run()

        print()
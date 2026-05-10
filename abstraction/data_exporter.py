"""
Exercise 2: Data Exporter
Design Data Exporter Class
Problem: Build a data export system where the abstract class provides shared validation logic, 
and subclasses handle the actual export format.

Requirements:

Abstract DataExporter class with: a concrete validate(data) method that checks 
if data is not null/empty and prints a validation message, plus an abstract export(data) method

CSVExporter: formats data as comma-separated values
JSONExporter: formats data as a JSON array
The validate() method should be called inside export() before formatting, so all exporters validate automatically
"""

# CSV
# Call self.validate(data) first. If validation fails, return early.
        # Otherwise, print CSV format: "CSV: Alice,Bob,Charlie"
        # Hint: use ",".join(data)


# JSON
# Call self.validate(data) first. If validation fails, return early.
        # Otherwise, print JSON array format: JSON: ["Alice", "Bob", "Charlie"]


from abc import ABC, abstractmethod

class DataExporter(ABC):
    def validate(self, data: list) -> bool:
        if data:
            print("Data is not Null")
            return True
        else:
            print("Data is Null")
            return False
    
    @abstractmethod
    def export(self, data: list) -> None:
        pass

class CSVExporter(DataExporter):
    def export(self, data: list) -> None:
        if self.validate(data):
            print(",".join(data))
        else:
            return
        

class JSONExporter(DataExporter):
    def export(self, data: list) -> None:
        if self.validate(data):
            print(f"JSON: {data}")
        else:
            return
        

if __name__ == "__main__":
    csv = CSVExporter()
    csv.export(["Alice", "Bob", "Charlie"])

    print()

    json_exp = JSONExporter()
    json_exp.export(["Alice", "Bob", "Charlie"])

    print()

    csv.export([])  # Should fail validation
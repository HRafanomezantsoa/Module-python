#! /usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data_list: list[tuple[int, str]] = []
        self._index: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data_list:
            raise IndexError("No data.")
        return self._data_list.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(isinstance(x, (int, float)) and not isinstance(
                        data, bool) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        values = data if isinstance(data, list) else [data]
        for value in values:
            self._data_list.append((self._index, str(value)))
            self._index += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        values = data if isinstance(data, list) else [data]
        for value in values:
            self._data_list.append((self._index, value))
            self._index += 1


class LogProcessor(DataProcessor):
    def validate_dict(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        return all(
            isinstance(
                k, str
                ) and isinstance(v, str) for k, v in data.items())

    def validate(self, data: Any) -> bool:
        if self.validate_dict(data):
            return True
        if isinstance(data, list):
            if len(data) == 0:
                return False
            return all(self.validate_dict(x) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        values = data if isinstance(data, list) else [data]
        for value in values:
            key = value.get('log_level')
            val = value.get('log_message')
            log_value = f"{key}: {val}"
            self._data_list.append((self._index, log_value))
            self._index += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numProcess = NumericProcessor()
    print(f" Trying to validate input '42': {numProcess.validate(42)}")
    print(f" Trying to validate input 'Hello': {numProcess.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numProcess.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f" Got exception: {e}")
    print(" Processing data : [1, 2, 3, 4, 5]")
    numProcess.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = numProcess.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    textProcess = TextProcessor()
    print(f" Trying to validate input '42': {textProcess.validate(42)}")
    data: list[str] = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {data}")
    print(" Extracting 1 value...")
    textProcess.ingest(data)
    for _ in range(1):
        rank, value = textProcess.output()
        print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    logProcess = LogProcessor()
    print(f" Trying to validate input 'Hello'\
: {logProcess.validate('Hello')}")
    notice: dict[str, str] = {
        'log_level': 'NOTICE',
        'log_message': 'Connection to server'
    }
    error: dict[str, str] = {
        'log_level': 'ERROR',
        'log_message': 'Unauthorized access!!'
    }
    logs: list[dict[str, str]] = [notice, error]
    print(f" Processing data: {logs}")
    logProcess.ingest(logs)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = logProcess.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

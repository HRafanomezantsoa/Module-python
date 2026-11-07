#! /usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data_list: list[tuple[int, str]] = []
        self._index: int = 0
        self._processor: int = 0

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

    def stats(self) -> None:
        name = self.__class__.__name__.replace("Processor", " Processor")
        print(f"{name}: total {self._processor} items processed,\
 remaining {len(self._data_list)} on processor")


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
            self._processor += 1


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
            self._processor += 1


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
            self._processor += 1


class DataStream:
    def __init__(self) -> None:
        self._data_processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._data_processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        if self._data_processors:
            for data in stream:
                for processor in self._data_processors:
                    if processor.validate(data):
                        processor.ingest(data)
                        break
                else:
                    print(f"DataStream error -\
 Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._data_processors:
            print("No processor found, no data\n")
        else:
            for processor in self._data_processors:
                processor.stats()


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    data_stream: list[Any] = [
        "Hello world", [3.14, -1, 2.71],
        [{"log_level": "WARNING",
          "log_message": "Telnet access! Use ssh instead"},
         {"log_level": "INFO", "log_message": "User wil is connected"}],
        42, ['Hi', 'five']]
    print("Initialize Data Stream...")
    dataStream = DataStream()
    numProcess = NumericProcessor()
    textProcess = TextProcessor()
    logProcess = LogProcessor()
    dataStream.process_stream(data_stream)
    dataStream.print_processors_stats()
    print("Registering Numeric Processor\n")
    print(f"Send first batch of data on stream: {data_stream}")
    dataStream.register_processor(numProcess)
    dataStream.process_stream(data_stream)
    dataStream.print_processors_stats()
    print("\nRegistering other data processors")
    print("Send the same batch again")
    dataStream.register_processor(textProcess)
    dataStream.register_processor(logProcess)
    dataStream.process_stream(data_stream)
    dataStream.print_processors_stats()
    print("\nConsume some elements from the data processors:\
 Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numProcess.output()
    for _ in range(2):
        textProcess.output()
    for _ in range(1):
        logProcess.output()
    dataStream.print_processors_stats()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

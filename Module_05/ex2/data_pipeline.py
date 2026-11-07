#! /usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


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

    def output(self, count: int) -> list[tuple[int, str]]:
        if not self._data_list:
            raise IndexError("No data.")
        delete: list[tuple[int, str]] = []
        for _ in range(count):
            if self._data_list:
                delete.append(self._data_list.pop(0))
        return delete

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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        value: list[str] = [v for _, v in data]
        csv: str = ",".join(value)
        print(f"CSV Output:\n{csv}")


class JSONPuglin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        value = [f'"item_{k}": "{v}"' for k, v in data]
        json: str = "{" + ", ".join(value) + "}"
        print(f"JSON Output:\n{json}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._data_processors:
            data = processor.output(nb)
            if data:
                plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    data_stream: list[Any] = [
        "Hello world", [3.14, -1, 2.71],
        [{"log_level": "WARNING",
          "log_message": "Telnet access! Use ssh instead"},
         {"log_level": "INFO", "log_message": "User wil is connected"}],
        42, ['Hi', 'five']]
    print("Initialize Data Stream...\n")
    dataStream = DataStream()
    numProcess = NumericProcessor()
    textProcess = TextProcessor()
    logProcess = LogProcessor()
    dataStream.process_stream(data_stream)
    dataStream.print_processors_stats()
    print("Registering Processors\n")
    print(f"Send first batch of data on stream: {data_stream}\n")
    dataStream.register_processor(numProcess)
    dataStream.register_processor(textProcess)
    dataStream.register_processor(logProcess)
    dataStream.process_stream(data_stream)
    dataStream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv = CSVPlugin()
    dataStream.output_pipeline(3, csv)
    print()
    dataStream.print_processors_stats()
    another_data: list[Any] = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"\nSend another batch of data:{another_data}\n")
    dataStream.process_stream(another_data)
    dataStream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json = JSONPuglin()
    dataStream.output_pipeline(5, json)
    print()
    dataStream.print_processors_stats()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

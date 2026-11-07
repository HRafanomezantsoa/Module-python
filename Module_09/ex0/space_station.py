try:
    from pydantic import BaseModel, Field, ValidationError
    from datetime import datetime
except ImportError as e:
    print(e)


class Validat_station(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def test_valid() -> None:
    print("========================================")
    try:
        station = Validat_station(
            station_id="ISS001",
            name="International Space Station",
            crew_size=20,
            power_level=85.5,
            oxygen_level=92.3,
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status: str = (
            "Operational" if station.is_operational
            else "Non-operational")
        print(f"Status: {status}")
    except ValidationError as e:
        print("Expected validation error:")
        print(f"{e.errors()[0]['loc'][0]} : {e.errors()[0]['msg']}")


def test_invalid() -> None:
    print("========================================")
    try:
        station = Validat_station(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}")
        print(f"Oxygen: {station.oxygen_level}")
        status: str = (
            "Operational" if station.is_operational
            else "Non-operational")
        print(f"Status: {status}")
    except ValidationError as e:
        print("Expected validation error:")
        print(f"{e.errors()[0]['loc'][0]} : {e.errors()[0]['msg']}")


def main() -> None:
    print("Space Station Data Validation")
    test_valid()
    print()
    test_invalid()


if __name__ == "__main__":
    main()

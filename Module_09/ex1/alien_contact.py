try:
    from enum import Enum
    from pydantic import BaseModel, Field, ValidationError, model_validator
    from datetime import datetime
except ImportError as e:
    print(e)


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def model_valid(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
             self.contact_type == ContactType.TELEPATHIC and
             not self.witness_count > 3):
            raise ValueError("Telepathic contact \
requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) \
should include received messages")
        return self


def test_valid() -> None:
    print("======================================")
    try:
        validation = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print("Valid contact report:")
        print(f"ID: {validation.contact_id}")
        print(f"Type: {validation.contact_type.value}")
        print(f"Location: {validation.location}")
        print(f"Signal: {validation.signal_strength}/10")
        print(f"Duration: {validation.duration_minutes} minutes")
        print(f"Witnesses: {validation.witness_count}")
        print(f"Message: '{validation.message_received}'")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


def test_invalid() -> None:
    print("======================================")
    try:
        validation = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
        )
        print("Alien Contact Log Validation")
        print("Valid contact report:")
        print(f"ID: {validation.contact_id}")
        print(f"Type: {validation.contact_type.value}")
        print(f"Location: {validation.location}")
        print(f"Signal: {validation.signal_strength}/10")
        print(f"Duration: {validation.duration_minutes} minutes")
        print(f"Witnesses: {validation.witness_count}")
        print(f"Message: '{validation.message_received}'")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


def main() -> None:
    print("Alien Contact Log Validation")
    test_valid()
    print()
    test_invalid()


if __name__ == "__main__":
    main()

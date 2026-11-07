try:
    from enum import Enum
    from pydantic import Field, BaseModel, model_validator, ValidationError
    from datetime import datetime
except ImportError as e:
    print(e)


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        valid_rank = any(
            member.rank in [Rank.COMMANDER, Rank.CAPTAIN]
            for member in self.crew
        )
        if not valid_rank:
            raise ValueError("Mission must have \
at least one Commander or Captain")
        if self.duration_days > 365:
            members = len(self.crew)
            experienced = sum(
                1 for member in self.crew
                if member.years_experience >= 5)
            percent = (experienced / members) * 100
            if percent < 50:
                raise ValueError(
                    "Long missions (> 365 days) \
need 50% experienced crew (5+ years)"
                )
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def test_valid() -> None:
    try:
        crew1 = CrewMember(
            name="Sarah Connor",
            member_id="M2024_MARS",
            rank=Rank.COMMANDER,
            age=18,
            specialization="Mission Command",
            years_experience=5,
            is_active=True,
        )
        crew2 = CrewMember(
            name="John Smith",
            member_id="M2024_MARS",
            rank=Rank.LIEUTENANT,
            age=19,
            specialization="Navigation",
            years_experience=6,
            is_active=True,
        )

        crew3 = CrewMember(
            name="Alice Johnson",
            member_id="M2024_MARS",
            rank=Rank.OFFICER,
            age=20,
            specialization="Engineering",
            years_experience=3,
            is_active=True,
        )
        space = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=[crew1, crew2, crew3],
        )
        print("Valid mission created:")
        print(f"Mission: {space.mission_name}")
        print(f"ID: {space.mission_id}")
        print(f"Destination: {space.destination}")
        print(f"Duration: {space.duration_days} days")
        print(f"Budget: ${space.budget_millions}M")
        print(f"Crew size: {len(space.crew)}")
        print("Crew members:")
        for i in space.crew:
            print(f"- {i.name} ({i.rank.value}) - {i.specialization}")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


def test_invalid() -> None:
    try:
        crew1 = CrewMember(
            name="Sarah Connor",
            member_id="M2024_MARS",
            rank=Rank.OFFICER,
            age=18,
            specialization="Mission Command",
            years_experience=5,
        )
        crew2 = CrewMember(
            name="John Smith",
            member_id="M2024_MARS",
            rank=Rank.LIEUTENANT,
            age=19,
            specialization="Navigation",
            years_experience=6,
        )

        crew3 = CrewMember(
            name="Alice Johnson",
            member_id="M2024_MARS",
            rank=Rank.OFFICER,
            age=20,
            specialization="Engineering",
            years_experience=3,
        )
        space = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=[crew1, crew2, crew3],
        )
        print("Valid mission created:")
        print(f"Mission: {space.mission_name}")
        print(f"ID: {space.mission_id}")
        print(f"Destination: {space.destination}")
        print(f"Duration: {space.duration_days} days")
        print(f"Budget: ${space.budget_millions}M")
        print(f"Crew size: {len(space.crew)}")
        print("Crew members:")
        for i in space.crew:
            print(f"- {i.name} ({i.rank.value}) - {i.specialization}")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    print("=========================================")
    test_valid()
    print("\n=========================================")
    test_invalid()

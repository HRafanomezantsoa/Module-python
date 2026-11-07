#! /usr/bin/env python3
from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(ABC):
    name: str = ""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}' \
for this {self.name} strategy"
            )
        return ""


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        super().act(creature)
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    name = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        super().act(creature)
        c = cast(TransformCapability, creature)
        return "\n".join([
            c.transform(),
            creature.attack(),
            c.revert()
        ])


class DefensiveStrategy(BattleStrategy):
    name = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        super().act(creature)
        c = cast(HealCapability, creature)
        return "\n".join([
            creature.attack(),
            c.heal()
        ])

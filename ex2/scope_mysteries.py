from typing import Any


def mage_counter() -> callable:
    """
    Return a closure function that counts how many times it has been called
    """
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    """Return a closure function that accumulates power over time"""
    power = initial_power

    def accumulator(new_power: int) -> int:
        nonlocal power
        power += new_power
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    """Return a closure function that applies the specified enchantment type"""
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, callable]:
    """
    Return a dictionary 'store' and 'recall' for private memory management
    """
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    return {
        "store": store,
        "recall": lambda key: memory.get(key, "Memory not found")
    }


def main() -> None:
    """Execute tests for Memory Depths closures."""
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator...")
    accum = spell_accumulator(12)
    print(f"Call 1: {accum(12)}")
    print(f"Call 2: {accum(3)}")
    print(f"Call 3: {accum(5)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("Flaming", "Sword")
    print(vault["recall"]("Flaming"))
    print(vault["recall"]("Frozen"))
    vault["store"]("Frozen", "Shield")
    print(vault["recall"]("Frozen"))


if __name__ == "__main__":
    main()

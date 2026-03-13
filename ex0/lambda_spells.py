def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power level in descending order"""
    return sorted(artifacts, key=lambda a: a.get("power", 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Filter mages with a power level greater than or equal to min_power
    """
    return list(filter(lambda m: m.get("power", 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform a list of spell names by adding asterisks as a prefix and suffix
    """
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    Calculate and return the maximum, minimum, and average power levels
    """
    return {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda x: x["power"])["power"],
        "avg_power": round(sum(map(
            lambda x: x["power"], mages
            )) / len(mages), 2)
    }


def main() -> None:
    """Execute tests for Lambda Sanctum spells."""
    print("Testing artifact sorter...")

    artifacts = [
        {'name': 'Water Chalice', 'power': 80, 'type': 'focus'},
        {'name': 'Wind Cloak', 'power': 83, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 118, 'type': 'relic'},
        {'name': 'Wind Cloak', 'power': 99, 'type': 'armor'}
    ]

    mages = [
        {'name': 'Ember', 'power': 100, 'element': 'wind'},
        {'name': 'Storm', 'power': 80, 'element': 'fire'},
        {'name': 'Riley', 'power': 87, 'element': 'wind'},
        {'name': 'River', 'power': 56, 'element': 'fire'},
        {'name': 'Ember', 'power': 55, 'element': 'ice'}
    ]

    spells = ['lightning', 'darkness', 'heal', 'tornado']

    print("Before sorting:")
    print(artifacts)
    print()

    print("After sorting:")
    print(artifact_sorter(artifacts))
    print()

    print("Testing power filter...")
    print("Showing powers:")
    print(mages)
    print()

    print("Showing power filter:")
    print(power_filter(mages, 80))
    print()

    print("Testing spell transformer...")

    print("Before transformation:")
    print(spells)
    print()

    print("After transformation:")
    print(spell_transformer(spells))
    print()

    print("Testing mage stats...")
    print("Showing mages again:")
    print(mages)
    print()

    print("Showing stats:")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()

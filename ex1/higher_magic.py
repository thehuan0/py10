def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """
    Combine into a single function that returns a tuple of both results
    """
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs)
    )


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    Return a new function that multiplies the base result by the multiplier
    """
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    Return a function that only casts the spell if the condition returns True
    """
    return lambda *args, **kwargs: (
        spell(*args, **kwargs) if condition(*args, **kwargs)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[callable]) -> callable:
    """Return a function that casts all spells in the sequence in order"""
    return lambda *args, **kwargs: [
        spell(*args, **kwargs) for spell in spells
    ]


def main() -> None:
    """Execute tests for Higher Realm spells."""
    print("Testing spell combiner...")

    def fireball(creature):
        return f"Fireball hits {creature}"

    def heal(creature):
        return f"Heals {creature}"

    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {', '.join(combined('dragon'))}")

    print("\nTesting power amplifier...")

    def power(x):
        return 2 * x - 4

    amplified = power_amplifier(power, 3)
    print(f"Original: {power(7)}, Amplified: {amplified(7)}")

    print("\nTesting conditional caster...")

    def spell(x):
        return f"Deal {x} damage"

    def condition(x):
        return x % 2 == 0

    conditional_spell = conditional_caster(condition, spell)
    print(f"True condition: {conditional_spell(6)}")
    print(f"False condition: {conditional_spell(5)}")

    print("\nTesting spell sequence...")

    def spell1(x, y):
        return x + y

    def spell2(x, y):
        return x - y

    def spell3(x, y):
        return x * y

    sequence = spell_sequence([spell1, spell2, spell3])
    print(f"Spell sequence with inputs 5 and 2: {sequence(5, 2)}")


if __name__ == "__main__":
    main()

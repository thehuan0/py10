from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Combine all spell powers using functools.reduce and a specified operation.
    """
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    f = ops.get(operation)
    if not f:
        return 0
    return reduce(f, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    Create a dictionary of enchantment functions using functools.partial
    """
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(
            base_enchantment, power=50, element="lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number with lru_cache decorator for memoization
    """
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """
    Create a single dispatch system to handle different types of spells
    """
    @singledispatch
    def spell(s) -> str:
        return f"Unknown spell {s}"

    @spell.register
    def _(s: int) -> str:
        return f"{s} damage delt"

    @spell.register
    def _(s: str) -> str:
        return f"{s} enchantment"

    @spell.register
    def _(s: list) -> str:
        return [spell(item) for item in s]
    return spell


def main() -> None:
    """Execute tests for Ancient Library functools treasures."""
    print("Testing spell reducer...")
    spell_powers = [46, 48, 21, 40, 34, 12]
    operations = ['add', 'multiply', 'max', 'min']
    print(spell_powers)
    for operation in operations:
        print(
            f"{operation.capitalize()}: "
            f"{spell_reducer(spell_powers, operation)}"
        )

    print("\nTesting partial enchanter...")

    def general_enchantment(target, power, element):
        return f"A {element} enchantment of power {power} hit {target}"

    enchantments = partial_enchanter(general_enchantment)
    print(enchantments['fire_enchant']('dragon'))
    print(enchantments['ice_enchant']('goblin'))
    print(enchantments['lightning_enchant']('magician'))

    print("\nTesting memoized fibonacci...")
    fibonacci_tests = [11, 19, 11]
    for f in fibonacci_tests:
        print(f"Fib({f}): {memoized_fibonacci(f)}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell("Fire"))
    print(spell(11))
    print(spell(["Fire", 19, 11, "Ice"]))


if __name__ == "__main__":
    main()

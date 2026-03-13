from functools import wraps
import time
import random
import inspect


def spell_timer(func: callable) -> callable:
    """Decorator that measures and prints a function's execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """
    Decorator factory that validates if the spell is cast with adequate power.
    """
    def decorator_func(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            power_val = bound_args.arguments.get("power")
            if power_val is None and args:
                power_val = args[0]
            if power_val is not None and power_val >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator_func


def retry_spell(max_attempts: int) -> callable:
    """
    Decorator that retries a failed function call up
    """
    def decorator_func(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {i + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator_func


class MageGuild:
    """
    Class representing the Mage Guild to demonstrate staticmethod capabilities.
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Static method that checks if a mage's name is valid"""
        return all(c.isalpha() or c.isspace() for c in name) and len(name) > 2

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        Instance method utilizing the power_validator decorator to cast a spell
        """
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Execute tests for Master's Tower decorators."""
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        return "Fireball cast!"
    print(fireball())

    print("\nTesting power validator...")

    @power_validator(5)
    def spell(power, name):
        return f"{name} spell casted with power {power}!"

    print(spell(9, "darkness"))
    print(spell(2, "earthquake"))
    print(spell(8, "shield"))
    print(spell(7, "fireball"))

    print("\nTesting retry spell...")

    @retry_spell(3)
    def random_spell():
        if random.randint(0, 2) == 0:
            return "SPELL CASTED"
        else:
            raise ValueError
    print(random_spell())
    print(random_spell())
    print(random_spell())

    print("\nTesting MageGuild...")
    mage_names = ['Jordan', 'Ash', 'Rowan', 'Phoenix', 'Zara', 'River']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']
    print(all(MageGuild.validate_mage_name(mage) for mage in mage_names))
    print(any(MageGuild.validate_mage_name(mage) for mage in invalid_names))

    mage = MageGuild()
    print(mage.cast_spell('Darkness', 13))
    print(mage.cast_spell('Fireball', 6))


if __name__ == "__main__":
    main()

def convert_from_decimal(decimal_value: int):
    """Convert from decimal to binary, octal, and hexadecimal"""
    return {
        "Decimal": str(decimal_value),
        "Binary": bin(decimal_value)[2:],
        "Octal": oct(decimal_value)[2:],
        "Hexadecimal": hex(decimal_value)[2:].upper()
    }

def convert_number(number: str, base: str):
    """Convert number from a given base to all other number systems"""
    try:
        if base == "binary":
            decimal_value = int(number, 2)
        elif base == "octal":
            decimal_value = int(number, 8)
        elif base == "hexadecimal":
            decimal_value = int(number, 16)
        elif base == "decimal":
            decimal_value = int(number)
        else:
            return "Invalid base selection."

        return convert_from_decimal(decimal_value)

    except ValueError:
        return f"Invalid {base} number input."


def main():
    print("=== Number System Converter ===")
    print("You can convert between Binary, Decimal, Octal, and Hexadecimal.")
    print("Choose base type: binary | decimal | octal | hexadecimal")

    base = input("Enter base type: ").strip().lower()
    number = input(f"Enter your {base} number: ").strip()

    result = convert_number(number, base)

    if isinstance(result, dict):
        print("\nConversion Results:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)


if __name__ == "__main__":
    main()

class PowerCalculator:
    class InvalidInputException(Exception):
        def __init__(self, base, power) -> None:
            self.base = base
            self.power = power
            self.message = f"Некорректный ввод: {base} в степени {power}. Основание должно быть числом, отличным от 0, степень должна быть положительным числом"
            super().__init__(self.message)

    def calculatePower(self, base: str, power: str):
        try:
            self.base = int(base)
            self.power = int(power)
            if self.base == 0 or self.power < 0:
                raise self.InvalidInputException(base, power)
            return self.base ** self.power
        except ValueError:
            raise self.InvalidInputException(base, power)


def main():
    pcalc = PowerCalculator()

    base = input("Введите основание: ")
    power = input("Введите степень: ")
    print(pcalc.calculatePower(base, power))


if __name__ == "__main__":
    main()

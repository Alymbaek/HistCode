
class InvalidkeyError(Exception):
    pass
class UnitConverter:
    def __init__(self) -> None:
        self.units = {
            'm': {'m': 1.0, 'km': 0.001, 'mi': 0.000621371, 'ft': 3.28084},
            'km': {'m': 1000.0, 'km': 1.0, 'mi': 0.621371, 'ft': 3280.84},
            'mi': {'m': 1609.34, 'km': 1.60934, 'mi': 1.0, 'ft': 5280},
            'ft': {'m': 0.3048, 'km': 0.0003048, 'mi': 0.000189394, 'ft': 1.0},
        }

    def convert(self, from_unit, to_unit, value) -> float:
        try:
            from_unit_dict = self.units[from_unit]
            to_unit_coef = from_unit_dict[to_unit]
            return value * to_unit_coef
        except KeyError:
          raise InvalidkeyError('Тура эмес бирдик')

    def get_units(self):
        return sorted(self.units.keys())


conv = UnitConverter()
res = conv.get_units()
print(res)
print('URA!')





























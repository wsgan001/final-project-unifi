"""Discretization of countinous attributes in datasets."""

class _DiscRange:
    def __init__(self, minimum, maximum):
        self.label = str(minimum) + '-' + str(maximum)
        self._min = minimum
        self._max = maximum

    def in_range(self, value):
        """Are you happy, damned linter? What could this function possibly do?"""
        return self._min <= value <= self._max


VAL_SCORE = {_DiscRange(0, 4), _DiscRange(4, 6), _DiscRange(6, 7),
             _DiscRange(7, 8), _DiscRange(8, 10)}
STD_DEV = {_DiscRange(0, 1), _DiscRange(1, 2), _DiscRange(2, 3.5),
           _DiscRange(3.5, 5), _DiscRange(5, 6.5)}
MARKS = {_DiscRange(18, 22), _DiscRange(22, 24), _DiscRange(24, 26), _DiscRange(26, 28),
         _DiscRange(28, 31)}

ZERO_TO_HUND = {_DiscRange(0, 20), _DiscRange(20, 40), _DiscRange(40, 60), _DiscRange(60, 80),
                _DiscRange(80, 100), _DiscRange(100, 120)}


def _discretize(value, ranges):
    if value == 'n.c.' or value == '<5':
        return value.upper()

    range_found = False

    for rng in ranges:
        if rng.in_range(float(value)):
            value = rng.label
            range_found = True
            break

    if not range_found:
        value = 'OUT_OF_RANGE'

    return value


def discretize(source, dest, keys, ranges, drop):
    """Discretization of countinous attributes in datasets.
    WARNING: keys and ranges must match positionally!"""
    if len(keys) != len(ranges):
        raise Exception('Keys and ranges length are different!')

    for doc in source.find():
        source.delete_one(doc)

        for i in range(len(keys)):
            doc[keys[i]] = _discretize(doc[keys[i]], ranges[i])

        dest.insert_one(doc)

    if drop == 'Y':
        source.drop()
from collections import namedtuple
from collections import defaultdict

Params = namedtuple('Region', ('subrectangle', 'grayscale'))

class DataInput:
    def __init__(self):
        self._params = []

    def add_params(self, subrectangle, grayscale):
        self._params.append(Params(subrectangle, grayscale))


class Regions:
    def __init__(self):
        self._regions = defaultdict(DataInput)

    def add_regions(self, region):
        return self._regions[region]

    def print_regions(self):
        for item in self._regions.values():
            print(item)

  
region = Regions()
region1 = region.add_regions("region1")
region1.add_params((0, 0, 0), (100, 100, 100))

region.print_regions()
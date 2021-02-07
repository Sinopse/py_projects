from collections import namedtuple
from collections import defaultdict

Params = namedtuple('Region', ('subrectangle', 'grayscale'))

class DataInput:
    def __init__(self, region):
        self._regions = {}
        self._params = []
        self.region = region

    def add_params(self, subrectangle, grayscale):
        self._params.append(Params(subrectangle, grayscale))
        self._regions[self.region] = self._params


data = DataInput("region1")
data.add_params((0, 0, 0), (100, 100, 100))

for key, val in data._regions.items():
    print(key, val)

# data.add_params((0, 0, 0, 0), (100, 100, 100))

print(data._regions["region1"][0].subrectangle)
print(data._regions["region1"][0].grayscale)

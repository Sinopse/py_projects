from collections import defaultdict

# gray scale as const in a dict
# check for missing keys and values -> effective python
_GRAYSCALE = {'gray1': (15, 15, 15),
              'gray2': (55, 55, 55),
              'gray3': (95, 95, 95),
              'gray4': (127, 127, 127),
              'gray5': (159, 159, 159),
              'gray6': (199, 199, 199)}


class ConfigData:
    def __init__(self, region):
        self.region = region
        self._regions = defaultdict(list)

    def add_params(self, subrectangle, grayscale):
        if isinstance(subrectangle, tuple) and len(subrectangle) == 4:
            self._regions[self.region].append(subrectangle)
            self._regions[self.region].append(_GRAYSCALE[grayscale])
        else:
            raise TypeError("Inappropriate container types - supply a tuple")

container = []

data = ConfigData("region1")
data.add_params((0, 0, 800, 330), "gray4")
data.add_params((800, 0, 1280, 330), "gray2")

container.append(data)

# multiple dictionaries for multiple regions stored in a list?
# for config in list ...



# print(data._regions)

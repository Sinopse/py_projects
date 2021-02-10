from collections import defaultdict

# gray scale as const in a dict
# check for missing keys and values -> effective python
_GRAYSCALE = {'gray6': (15, 15, 15),
              'gray5': (55, 55, 55),
              'gray4': (95, 95, 95),
              'gray3': (127, 127, 127),
              'gray2': (159, 159, 159),
              'gray1': (199, 199, 199)}


class ConfigData:
    def __init__(self):
        self._regions = defaultdict(list)

    def add_params(self, region, subrectangle, grayscale):
        #if isinstance(subrectangle, tuple) and len(subrectangle) == 4:
            self._regions[region].append(subrectangle)
            self._regions[region].append(_GRAYSCALE[grayscale])
        #else:
         #   raise TypeError("Inappropriate container types - supply a tuple")

# config = ConfigData()
# config.add_params("region1", (0, 0, 2700, 1140), "gray2")
# config.add_params("region2", (0, 0, 2700, 1140), "gray3")
#
# print(config.__dict__)
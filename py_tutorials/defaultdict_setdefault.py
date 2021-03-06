from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()
visits.add('Russia', 'Moscow')
visits.add('Russia', 'Bryansk')
visits.add('Germany', 'Berlin')
visits.add('France', 'Paris')
print(visits.data['Russia'])

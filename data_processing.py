import csv, os

__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

class data_processing:

    def __init__(self) -> None:
        self.cities = []
        with open(os.path.join(__location__, 'Cities.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.cities.append(dict(r))

        self.countries = []
        with open(os.path.join(__location__, 'Countries.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.countries.append(dict(r))

        temps = []
        for city in self.cities:
            temps.append(float(city['temperature']))
        self.avg_temp = sum(temps)/len(temps)

    def get_avg_temp(self):
        # Print the average temperature of all the cities
        print("The average temperature of all the cities:")
        print(self.avg_temp)
        print()

    def print_all_cities(self, c: str = "Italy"):
        # Print all cities in Italy
        temps = []
        my_country = c
        for city in self.cities:
            if city['country'] == my_country:
                temps.append(city['city'])
        print("All the cities in", my_country, ":")
        print(temps)
        print()

    def print_avg_temp(self, c: str = "Italy"):
        # Print the average temperature for all the cities in Italy
        # Write code for me
        temps_temperature = []
        my_country = c
        for city in self.cities:
            if city['country'] == my_country:
                temps_temperature.append(float(city['temperature']))
        print("average temperature for all the cities in", my_country, ":")
        print(sum(temps_temperature)/len(temps_temperature))
        print()

    def max_temp(self, c: str = "Italy"):
        temps_temperature = []
        my_country = c
        for city in self.cities:
            if city['country'] == my_country:
                temps_temperature.append(float(city['temperature']))
        print("max temperature for all the cities in ", my_country, ":")
        print(max(temps_temperature))
        print()


    def call_filter(self):
        def filter(condition, dict_list):
            filtered_list = []
            for item in dict_list:
                if condition(item):
                    filtered_list.append(item)
            return filtered_list

        x = filter(lambda x: float(x['latitude']) >= 60.0, self.cities)
        for item in x:
            print(item)

    def aggregate(aggregation_key, aggregation_function, dict_list):
        values = [items[aggregation_key] for items in dict_list]
        return aggregation_function(values)

    def min_latitude(self, c: str = "Italy"):
        temps = []
        my_country = c
        for city in self.cities:
            if city['country'] == my_country:
                temps.append(float(city['latitude']))
        return min(temps)

    def max_latitude(self, c: str = "Italy"):
        temps = []
        my_country = c
        for city in self.cities:
            if city['country'] == my_country:
                temps.append(float(city['latitude']))
        return max(temps)


a = data_processing()

print("Average all cities tempurature is: " + str(a.avg_temp))
a.print_all_cities()
a.print_all_cities("Sweden")
a.print_avg_temp("Italy")
a.print_avg_temp("Sweden")
a.max_temp("Italy")
a.max_temp("Sweden")

print("##############################\n\n")
for i in a.cities:
    print(f"Min latitude in {i["country"]}:")
    print(a.min_latitude(i["country"]))
    print(f"Max latitude in {i["country"]}:")
    print(a.max_latitude(i["country"]))

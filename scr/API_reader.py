import json
with open("city.list.json", encoding="utf-8") as f:
    cities = json.load(f)
iran_cities = []
for city in cities:
    if city["country"] == "IR":
        iran_cities.append(city["name"])
iran_cities.sort()
# print(iran_cities)
# for city in iran_cities:
#     iran_name_city=[city["name"]]
# print(iran_cities)
print(iran_cities)

f = open("data5.txt")

seeds = []

N = 19090172320

seeds_to_soil = [*range(N)]
soil_to_fertilizer = [*range(N)]
fertilizer_to_water = [*range(N)]
water_to_light = [*range(N)]
light_to_temperature = [*range(N)]
temperature_to_humidity = [*range(N)]
humidity_to_location = [*range(N)]

l = []

for i,line in enumerate(f.readlines()):
    line = line.strip()
    if line == "" or line == "\n":
        pass

    elif i == 0:
        data = line.split(":")
        seeds = data[1].split()

    elif line == "seed-to-soil map:" : l = seeds_to_soil
    elif line == "soil-to-fertilizer map:" : l = soil_to_fertilizer
    elif line == "fertilizer-to-water map:" : l = fertilizer_to_water
    elif line == "water-to-light map:" : l = water_to_light
    elif line == "light-to-temperature map:" : l = light_to_temperature
    elif line == "temperature-to-humidity map:" : l = temperature_to_humidity
    elif line == "humidity-to-location map:" : l = humidity_to_location

    else :
        data = line.split()
        data = [int(i) for i in data]

        for i in range(data[2]):
            l[data[1]+i] = data[0]+i

        #print(data)

seeds2 = [[int(s)] for s in seeds]

for l in seeds2:
    l.append(seeds_to_soil[l[-1]])
    l.append(soil_to_fertilizer[l[-1]])
    l.append(fertilizer_to_water[l[-1]])
    l.append(water_to_light[l[-1]])
    l.append(light_to_temperature[l[-1]])
    l.append(temperature_to_humidity[l[-1]])
    l.append(humidity_to_location[l[-1]])

    #print(l)

locations = [l[-1] for l in seeds2]

#print("seeds = ",seeds2)
#print(locations)
print("min loc",min(locations))

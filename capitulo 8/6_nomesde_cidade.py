def city_country(city,country):

    places = f"{city},{country}"
    return places

world = city_country('Rio de Janeiro','\tBrasil')
print(world)

world = city_country('Toronto','Canadá')
print(world)

world = city_country('Tokyo','Japão')
print(world)

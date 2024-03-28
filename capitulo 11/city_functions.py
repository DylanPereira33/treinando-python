def get_city_country(city, country, população=""):
    if população:
        location = f"{city}, {country} – população {população}"
    else:
         location = f"{city}, {country}"
    return location.title()
    
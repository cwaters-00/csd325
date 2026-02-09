#chanceller waters
#2/6/26
#the purpose of this code is run and test for parameters given and display them in a formatted string

def city_country(city, country,population='', language=''):
    """Return a single string formatted with optional population and language. """
    output = f"{city.title()}, {country.title()}"
    if population:
        output += f" - population {population}"
    if language:
        output += f" , {language.title()}"
    return output


if __name__ == "__main__":
#calling function 3 times
    print(city_country("Santiago", "Chile"))
    print(city_country("Santiago", "Chile",500000))
    print(city_country("Santiago", "chile",500000,"spanish"))

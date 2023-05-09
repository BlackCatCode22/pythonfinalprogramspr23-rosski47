
import datetime

class Animal:
    def __init__(self, species, name, age, birth_season, color, gender, weight, origin):
        self.species = species
        self.name = name
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.gender = gender
        self.weight = weight
        self.origin = origin
        self.arrival_date = datetime.date.today()

        self.generate_id()

    def birthday_calc(season,age):
        # year counts from 2022 because these dates have not yet occurred in 2023
        year = 2022 - int(age.strip())
            # spring = "March 21"
            # summer = "June 21"
            # fall = "September 21"
            # winter = "December 21"
            # else = "July 21"
        if season.endswith("spring"):
            date = "March 21"
        elif season.endswith("summer"):
            date = "June 21"
        elif season.endswith("fall"):
            date = "September 21"
        elif season.endswith("winter"):
            date = "December 21"
        else:
            date = "July 21"
        birthday = date + ", " + str(year)
        return birthday

def lastWord(string):

    # split by space and converting
    # string to list and
    lis = list(string.split(" "))

    # length of list
    length = len(lis)

    # returning last element in list
    return lis[length - 1]

# uniqueID function adapted from approved solution file
def uniqueID(species, species_count):
    match species:
        case "hyena":
            prefix = "HY"
        case "lion":
            prefix = "LI"
        case "tiger":
            prefix = "TI"
        case "bear":
            prefix = "BE"
        case default:
            prefix = "XX"

    return prefix + "_0" + str(species_count)

def LineCountList(lines):
    line_count = 0
    list_of_lines = []
    for line in lines:
        print("Line " + str(line_count+1) + ":  " + line)
        line_count += 1
        list_of_lines.append(line)
    return list_of_lines

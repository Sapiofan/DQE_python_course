from OOP_HW4.HW4 import *
from String_HW3.HW3 import capitalize
import pathlib
import os

class InputChecker(InputHandling):
    # check if date is of correct format in the source file (dd/MM/yyyy hh:mm)
    @staticmethod
    def is_date(str_date, check_if_less_than_current = False):
        try:
            date = datetime.strptime(str_date.strip(), "%d/%m/%Y %H:%M")
            # uses this check if we need it only. Check if the date from file is behind the current time
            if check_if_less_than_current and date <= datetime.now():
                return False
            return True
        except ValueError:
            return False

    # check if the price is of correct format in the source
    @staticmethod
    def is_price(str_price):
        try:
            return True if float(str_price) else False
        except ValueError:
            return False

    # get valid path from user
    @staticmethod
    def get_valid_file_path():
        while True:
            file_path = input()
            if os.path.isfile(file_path):
                return file_path
            else:
                print("Invalid file path or file does not exist. Please try again.")

class FileHandler:

    # attempt to read the file
    def read_file(self, path = "source.txt"):
        try:
            f = open(path, "r")
            return f
        except:
            print("Something went wrong while reading the source file")

    # check if we have all needed attributes for entities and they are in incorrect format
    def check_file_format(self, file_text):
        entities = []
        for line in file_text:
            components = line.split(';')
            if components[0].lower() == "news":
                if len(components) == 4 and InputChecker.is_date(components[3]):
                    news = News(capitalize(components[1].lower()), capitalize(components[2].lower()))
                    news.set_publishing_date(convert_to_date(components[3]))
                    entities.append(news)
            elif components[0].lower() == "privatead":
                if len(components) == 3 and InputChecker.is_date(components[2], True):
                    ad = PrivateAd(capitalize(components[1].lower()),
                                   convert_to_date(components[2]))
                    entities.append(ad)
            elif components[0].lower() == "entertainment":
                if len(components) == 5 and InputChecker.is_date(components[4]) and InputChecker.is_price(components[3]):
                    ent = Entertainment(capitalize(components[1].lower()), capitalize(components[2].lower()), components[3],
                                        convert_to_date(components[4]))
                    entities.append(ent)

        return entities

    # add all entities in the target file
    def write_data_to_news(self, entities, output_path = 'output.txt'):
        for entity in entities:
            entity.publish(entity, output_path)

# convert dates from the source file to datetime type
def convert_to_date(string):
    return datetime.strptime(string.strip(), "%d/%m/%Y %H:%M")

# communication with user
def driver_hw6():
    print("Do you want to\n1. Import news data\n2. Input manually")
    user_choice = InputHandling.choose_category()
    match (user_choice):
        case 1:
            path = str(pathlib.Path(__file__).parent.resolve()) + "\\source.txt"
            print("Do you want to provide a path? Default path is: " + path)
            print("1. Yes\n2. No")
            path_choice = InputHandling.choose_category()

            if path_choice == 1:
                print("Input full path of the source file: ")
                path = InputChecker.get_valid_file_path()
            file_handler = FileHandler()
            if path_choice != 1:
                file = file_handler.read_file()
            else:
                file = file_handler.read_file(path)
            entities = file_handler.check_file_format(file)
            if len(entities) == 0:
                print("By the provided path the data isn't valid")
            else:
                file_handler.write_data_to_news(entities)
                print("All valid entities were added to the target file")
            file.close()
            # os.remove(path)
        case 2:
            driver()

if __name__ == '__main__':
    driver_hw6()

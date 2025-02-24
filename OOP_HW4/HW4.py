import time
from datetime import datetime

class WrongDateException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return self.args[0]

class Feed:
    def __init__(self, category):
        self.category = category
        self.publishing_date = datetime.now()
        self.line_limit = 25

    def publish(self, entity):
        string = self.category + ' '.ljust(self.line_limit, '-') + '\n' + str(entity)
        with open("output.txt", "a") as file:
            file.write(string + "\n\n")
        pass
class News(Feed):
    def __init__(self, text, city):
        super().__init__("News")
        self.text = text
        self.city = city

    def __str__(self):
        return f'{self.text}\n{self.city}, {self.publishing_date.strftime("%d/%m/%Y %H:%M")}'

class PrivateAd(Feed):
    def __init__(self, text, expiration_date):
        super().__init__("PrivateAd")
        self.text = text
        self.expiration_date = expiration_date

    def __str__(self):
        date_diff = self.expiration_date - self.publishing_date
        day_diff = date_diff.days
        return f'{self.text}\nActual until: {self.expiration_date.strftime("%d/%m/%Y %H:%M")}, {day_diff} days left'

class Entertainment(Feed):
    def __init__(self, description, place, price, time):
        super().__init__("Entertainment")
        self.text = description
        self.place = place
        self.price = price
        self.time = time

    def __str__(self):
        string = f"{self.text}\nWhere event will be conducted: {self.place}\nPrice: {self.price}\nStart at: {self.time}"
        return string

class InputHandling:
    @staticmethod
    def choose_category():
        while True:
            try:
                return int(input())
            except:
                print('Input number pls from the list. Try once again')

    @staticmethod
    def get_price():
        while True:
            user_input = input("Enter a decimal number: ")
            try:
                return round(float(user_input), 2)
            except ValueError:
                print("Invalid input. Please enter a valid decimal number.")

    @staticmethod
    def get_date_time():
        while True:
            try:
                date = datetime.strptime(input(), "%d/%m/%Y %H:%M")
                if date <= datetime.now():
                    raise WrongDateException('The date and time must be in the future. Please enter a valid date and time.')
                return date
            except ValueError:
                print("Invalid format. Please enter the date and time in dd/mm/yyyy HH:mm format.")
            except WrongDateException as e:
                print(e)

def driver():
    while True:
        print("Choose category for publishing:\n1. News\n2. PrivateAd\n3. Entertainment\n4. Quit")
        user_category = InputHandling.choose_category()
        match(user_category):
            case 1:
                print("Give the description of the news: ")
                text = input()
                print("Provide the city: ")
                city = input()
                news = News(text, city)
                news.publish(news)
            case 2:
                print("Give the description of the ad: ")
                text = input()
                print("Provide the expiration date in the format dd/mm/yyyy HH:mm ")
                expiration_date = InputHandling.get_date_time()
                ad = PrivateAd(text, expiration_date)
                ad.publish(ad)
            case 3:
                print("Give the description of the entertainment news: ")
                text = input()
                print("Provide the place of the event: ")
                place = input()
                print("Provide the price for input: ")
                price = InputHandling.get_price()
                print("Provide the time when it's started in the format dd/mm/yyyy HH:mm ")
                event_start = InputHandling.get_date_time()
                ent = Entertainment(text, place, price, event_start)
                ent.publish(ent)
            case _:
                break

driver()
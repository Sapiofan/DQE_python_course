from Modules_HW6.HW5 import *
import json


class JSONFileHandler(FileHandler):
    def check_json_format(self, records):
        entities = []
        for record in records:
            if "type" in record:
                if record["type"].lower() == "news" and all(k in record for k in ["posted", "place", "desc"]):
                    if InputChecker.is_date(record["posted"]):
                        news = News(capitalize(record["desc"].lower()), capitalize(record["place"].lower()))
                        news.set_publishing_date(convert_to_date(record["posted"]))
                        entities.append(news)
                elif record["type"].lower() == "privatead" and all(k in record for k in ["expired_at", "desc"]):
                    if InputChecker.is_date(record["expired_at"], True):
                        ad = PrivateAd(capitalize(record["desc"].lower()),
                                       convert_to_date(record["expired_at"]))
                        entities.append(ad)
                elif (record["type"].lower() == "entertainment"
                      and all(k in record for k in ["place", "desc", "price", "time"])):
                    if InputChecker.is_date(record["time"]) and InputChecker.is_price(
                            record["price"]):
                        ent = Entertainment(capitalize(record["desc"].lower()), capitalize(record["place"].lower()),
                                            record["price"], convert_to_date(record["time"]))
                        entities.append(ent)

        return entities


def driver_hw8():
    print("Do you want to\n1. Import news data\n2. Input manually")
    user_choice = InputHandling.choose_category()
    match (user_choice):
        case 1:
            path = str(pathlib.Path(__file__).parent.resolve()) + "\\source.json"
            print("Do you want to provide a path? Default path is: " + path)
            print("1. Yes\n2. No")
            path_choice = InputHandling.choose_category()

            if path_choice == 1:
                print("Input full path of the source file (.txt or .json extension): ")
                path = InputChecker.get_valid_file_path()
            file_handler = JSONFileHandler()
            file = file_handler.read_file(path)
            if ".json" in path:
                entities = file_handler.check_json_format(json.load(file))
            else:
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
    driver_hw8()

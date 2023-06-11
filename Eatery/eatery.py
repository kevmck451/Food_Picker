# Eatery Class

# name
# category
# takeout
# sitdown
# top dollar
# date night


class Eatery:
    def __init__(self, name, category, takeout, sitdown, top_dollar, date_night, tags_list):
        self.name = name
        self.category = category
        self.takeout = takeout
        self.sitdown = sitdown
        self.top_dollar = top_dollar
        self.date_night = date_night
        self.tags_list = tags_list


    def __str__(self):
        return f'Name: {self.name} / Category: {self.category}'



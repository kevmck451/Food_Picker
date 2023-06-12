# Code to deal with making a suggestion

import random
from Eatery.places import *


def get_full_list():
    return places_list


def filter_function(filter):
    if filter == 'Take Out':
        filter_list = [place for place in places_list if place.takeout]
    elif filter == 'Classics':
        filter_list = [place for place in places_list if 'classic' in place.tags_list]
    elif filter == 'Sit Down':
        filter_list = [place for place in places_list if place.sitdown]
    elif filter == 'Date Night':
        filter_list = [place for place in places_list if place.date_night]
    elif filter == 'Chicken':
        filter_list = [place for place in places_list if 'chicken' in place.tags_list]
    elif filter == 'Burgers':
        filter_list = [place for place in places_list if 'burgers' in place.tags_list]
    elif filter == 'Spicy':
        filter_list = [place for place in places_list if 'spicy' in place.tags_list]
    elif filter == 'Atmosphere':
        filter_list = [place for place in places_list if 'atmosphere' in place.tags_list]
    else:
        filter_list = []

    return filter_list


def make_suggestion(place_list):
    # Generate a random integer between start and end (inclusive)
    # Generate a random sample of unique indices
    indices = random.sample(range(len(place_list)), 3)
    index1, index2, index3 = indices

    # print(index1, index2, index3)

    places = [place_list[index1], place_list[index2], place_list[index3]]
    # print(places)
    return places







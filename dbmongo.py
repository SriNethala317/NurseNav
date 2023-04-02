from pymongo import MongoClient
from os import environ as env
from dotenv import find_dotenv, load_dotenv
from geopy.distance import geodesic

RANGE = 3
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

cluster = env.get("MONGODB_CLUSTER")
client = MongoClient(cluster)
db = client['nursenav']
users = db['users']
nurses = db['nurses']


def get_env():
    ENV_FILE = find_dotenv()
    if ENV_FILE:
        load_dotenv(ENV_FILE)
    return env

def all_tags():
    tags = []
    for nurse in list(nurses.find()):
        for tag in nurse['tags']:
            if tag not in tags:
                tags.append(tag)
    
    return tags

def find_nurses(location, tags):
    location = tuple(location)
    valid_nurses = []
    set_tags = set(tags)
    for nurse in list(nurses.find()):
        if set_tags.issubset(set(nurse['tags'])) and geodesic(location, tuple(nurse['location'])).mi < RANGE:
            valid_nurses.append(nurse)

    return valid_nurses

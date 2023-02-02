from pymongo import MongoClient
from data import users, projects
from datetime import datetime
from bson import ObjectId

client = MongoClient()
db = client.clockify_denormilized

users_collection = db.users
project_collection = db.projects
report_collection = db.reports


def store_once():
    users_collection.insert_many(users)
    project_collection.insert_many(projects)


def save_record():
    mohammad = users_collection.find_one({"username": "mohammad"})
    shop = project_collection.find_one({"name": "online shop"})

    report = report_collection.insert_one({
        "user": mohammad,
        "projects": shop,
        "start_time": datetime.now(),
    })


def set_end_time(obj_id):
    query = {"_id": ObjectId(obj_id)}
    update = {"$set": {"end_time": datetime.now()}}
    report_collection.update_one(query, update)


def show_reports():
    for report in report_collection.find():
        duration = report['end_time'] - report['start_time']
        print(f"{report['user']['username']}\t {report['projects']['name']}\t"
              f"{duration.seconds}")


if __name__ == "__main__":
    # save_record()
    # set_end_time("63dbd0d1feb865675bb40884")
    show_reports()
import pymongo
import os
from dotenv import load_dotenv, dotenv_values

# Database class to handle all MongoDB operations
class Database:


    # Constructor to initialize the MongoDB client and database
    def __init__(self):
        try:
            load_dotenv()

            # Connect to MongoDB Atlas
            self.client = pymongo.MongoClient(os.getenv("MONGO_URI")            )
            # Access the SecondRodeo database
            self.db = self.client["SecondRodeoData"]
            self.bull = self.db["bull"]
            self.calf = self.db["calf"]
            self.bronc = self.db["bronc"]
            self.steer = self.db["steer"]
            self.contractors = self.db["contractorcredentials"]
            print("Connected to MongoDB.\n")
        except Exception as e:
            print(f"An error occurred while connecting to MongoDB: {e}\n")

    # Method to insert a calf into the database
    def insertCalf(self, earTag, contractorName, kick, speed, direction):
        try:
            if kick == "True":
                kick = True
            else:
                kick = False
            # Create a calf dictionary
            calf = {
                "earTag": earTag,
                "organization": contractorName,
                "kick": kick,
                "speed": speed,
                "direction": direction
            }
            # Insert the calf into the collection
            self.db.calf.insert_one(calf)
            print("Calf inserted successfully.\n")
        except Exception as e:
            print(f"An error occurred while inserting calf: {e}\n")

    # Method to insert a bull into the database
    def insertBull(self, earTag, contractorName, straight, speed, direction):
        try:
            if straight == "True":
                straight = True
            else:
                straight = False
            # Create a bull dictionary
            bull = {
                "earTag": earTag,
                "organization": contractorName,
                "straight": straight,
                "speed": speed,
                "direction": direction
            }
            # Insert the bull into the collection
            self.db.bull.insert_one(bull)
            print("Bull inserted successfully.\n")
        except Exception as e:
            print(f"An error occurred while inserting bull: {e}\n")

    # Method to insert a steer into the database
    def insertSteer(self, earTag, contractorName, stop, speed, direction):
        try:
            if stop == "True":
                stop = True
            else:
                stop = False
            # Create a steer dictionary
            steer = {
                "earTag": earTag,
                "organization": contractorName,
                "stop": stop,
                "speed": speed,
                "direction": direction
            }
            # Insert the steer into the collection
            self.db.steer.insert_one(steer)
            print("Steer inserted successfully.\n")
        except Exception as e:
            print(f"An error occurred while inserting steer: {e}\n")


    # Method to insert a bronc into the database
    def insertBronc(self, earTag, contractorName, flankTightness, straight, speed, direction):
        try:
            if straight == "True":
                straight = True
            else:
                straight = False
            # Create a bronc dictionary
            bronc = {
                "earTag": earTag,
                "organization": contractorName,
                "flankTightness": int(flankTightness),
                "straight": straight,
                "speed": speed,
                "direction": direction
            }
            # Insert the bronc into the collection
            self.db.bronc.insert_one(bronc)
            print("Bronc inserted successfully.\n")
        except Exception as e:
            print(f"An error occurred while inserting bronc: {e}\n")


    # Method to retrieve all contractors from the database
    def getContractors(self):
        try:
            # Find all contractors in the collection
            contractors_cursor = self.contractors.find({}, {"_id": 0, "organization": 1})

            # Extract the contractor names into a list
            contractors_list = [contractor['organization'] for contractor in contractors_cursor]
            return contractors_list
        except Exception as e:
            print(f"An error occurred while retrieving contractors: {e}")
            return []  # Return an empty list in case of error
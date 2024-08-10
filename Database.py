import pymongo


# Database class to handle all MongoDB operations
class Database:


    # Constructor to initialize the MongoDB client and database
    def __init__(self):
        try:
            # Connect to MongoDB Atlas
            self.client = pymongo.MongoClient(
                "mongodb+srv://SecondRodeoPython:SecondRodeoPythonPassword@cluster0.ys6mzzd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            )
            # Access the SecondRodeo database
            self.db = self.client["SecondRodeo"]
            self.contractors = self.db["contractors"]
            print("Connected to MongoDB.\n")
        except Exception as e:
            print(f"An error occurred while connecting to MongoDB: {e}\n")


    # Method to add a contractor to the database
    def addContractor(self, contractorName):
        try:
            print(f"Attempting to add contractor: {contractorName}\n")
            # Insert the contractor with the provided name
            result = self.contractors.insert_one({
                "contractorName": contractorName,
                "stock": [
                    {"calfs": []},
                    {"steers": []},
                    {"bulls": []},
                    {"broncs": []}
                ]
            })
            print(f"Contractor added with ID: {result.inserted_id}")
        except Exception as e:
            print(f"An error occurred while adding the contractor: {e}")


    # Method to add a calf to the database
    def addCalf(self, earTag, contractorName, kick, speed, direction):
        try:
            # Check if the contractor with the given name
            contractor = self.contractors.find_one({"contractorName": contractorName})

            # If the contractor exists
            if contractor:
                # Check if the calf with the given earTag already exists
                result = self.contractors.update_one(
                    {
                        "contractorName": contractorName,
                        "stock.0.calfs.earTag": earTag
                    },
                    {
                        "$push": {
                            "stock.0.calfs.$.runInfo": {
                                "kick": kick,
                                "speed": speed,
                                "direction": direction
                            }
                        }
                    }
                )

                # If the calf does not exist, insert a new calf with the provided earTag and runInfo
                if result.matched_count == 0:
                    print(f"Adding new calf with earTag {earTag}...\n")
                    # Insert new calf with provided earTag and runInfo
                    result = self.contractors.update_one(
                        {"contractorName": contractorName},
                        {
                            "$push": {
                                "stock.0.calfs": {
                                    "earTag": earTag,
                                    "runInfo": [
                                        {
                                            "kick": kick,
                                            "speed": speed,
                                            "direction": direction
                                        }
                                    ]
                                }
                            }
                        },
                        upsert=True
                    )

                print(f"Update result: Matched {result.matched_count}, Modified {result.modified_count}\n")
            else:
                print("Contractor not found.\n")
        except Exception as e:
            print(f"An error occurred while adding the calf: {e}\n")


    # Method to add a steer to the database
    def addSteer(self, earTag, contractorName, stop, speed, direction):
        try:
            # Check if the contractor with the given name
            contractor = self.contractors.find_one({"contractorName": contractorName})

            # If the contractor exists
            if contractor:
                # Check if the steer with the given earTag already exists
                result = self.contractors.update_one(
                    {
                        "contractorName": contractorName,
                        "stock.1.steers.earTag": earTag
                    },
                    {
                        "$push": {
                            "stock.1.steers.$.runInfo": {
                                "stop": stop,
                                "speed": speed,
                                "direction": direction
                            }
                        }
                    }
                )

                # If the steer does not exist, insert a new steer with the provided earTag and runInfo
                if result.matched_count == 0:
                    print(f"Adding new steer with earTag {earTag}...\n")
                    result = self.contractors.update_one(
                        {"contractorName": contractorName},
                        {
                            "$push": {
                                "stock.1.steers": {
                                    "earTag": earTag,
                                    "runInfo": [
                                        {
                                            "stop": stop,
                                            "speed": speed,
                                            "direction": direction
                                        }
                                    ]
                                }
                            }
                        },
                        upsert=True
                    )

                print(f"Update result: Matched {result.matched_count}, Modified {result.modified_count}\n")
            else:
                print("Contractor not found.\n")
        except Exception as e:
            print(f"An error occurred while adding the steer: {e}\n")


    # Method to add a bull to the database
    def addBull(self, earTag, contractorName, straight, speed, direction):
        try:
            # Check if the contractor with the given name
            contractor = self.contractors.find_one({"contractorName": contractorName})

            # If the contractor exists
            if contractor:
                # Check if the bull with the given earTag already exists
                result = self.contractors.update_one(
                    {
                        "contractorName": contractorName,
                        "stock.2.bulls.earTag": earTag
                    },
                    {
                        "$push": {
                            "stock.2.bulls.$.runInfo": {
                                "straight": straight,
                                "speed": speed,
                                "direction": direction
                            }
                        }
                    }
                )

                # If the bull does not exist, insert a new bull with the provided earTag and runInfo
                if result.matched_count == 0:
                    print(f"Adding new bull with earTag {earTag}...")
                    result = self.contractors.update_one(
                        {"contractorName": contractorName},
                        {
                            "$push": {
                                "stock.2.bulls": {
                                    "earTag": earTag,
                                    "runInfo": [
                                        {
                                            "straight": straight,
                                            "speed": speed,
                                            "direction": direction
                                        }
                                    ]
                                }
                            }
                        },
                        upsert=True
                    )
                print(f"Update result: Matched {result.matched_count}, Modified {result.modified_count}\n")
            else:
                print("Contractor not found.\n")
        except Exception as e:
            print(f"An error occurred while adding the bull: {e}\n")


    # Method to add a bronc to the database
    def addBronc(self, earTag, contractorName, straight, speed, direction,  flankTightness):
        try:
            # Check if the contractor with the given name
            contractor = self.contractors.find_one({"contractorName": contractorName})

            # If the contractor exists
            if contractor:
                # Check if the bronc with the given earTag already exists
                result = self.contractors.update_one(
                    {
                        "contractorName": contractorName,
                        "stock.3.broncs.earTag": earTag
                    },
                    {
                        "$push": {
                            "stock.3.broncs.$.runInfo": {
                                "straight": straight,
                                "speed": speed,
                                "direction": direction,
                                "flankTightness": flankTightness
                            }
                        }
                    }
                )

                # If the bronc does not exist, insert a new bronc with the provided earTag and runInfo
                if result.matched_count == 0:
                    print(f"Adding new bronc with earTag {earTag}...")
                    result = self.contractors.update_one(
                        {"contractorName": contractorName},
                        {
                            "$push": {
                                "stock.3.broncs": {
                                    "earTag": earTag,
                                    "runInfo": [
                                        {
                                            "straight": straight,
                                            "speed": speed,
                                            "direction": direction,
                                            "flankTightness": flankTightness
                                        }
                                    ]
                                }
                            }
                        },
                        upsert=True
                    )

                print(f"Update result: Matched {result.matched_count}, Modified {result.modified_count}\n")
            else:
                print("Contractor not found.\n")
        except Exception as e:
            print(f"An error occurred while adding the bronc: {e}\n")


    # Method to retrieve all contractors from the database
    def getContractors(self):
        try:
            # Find all contractors in the collection
            contractors_cursor = self.contractors.find({}, {"_id": 0, "contractorName": 1})

            # Extract the contractor names into a list
            contractors_list = [contractor['contractorName'] for contractor in contractors_cursor]
            return contractors_list
        except Exception as e:
            print(f"An error occurred while retrieving contractors: {e}")
            return []  # Return an empty list in case of error


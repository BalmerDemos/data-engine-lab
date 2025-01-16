import json
import os
import logging
from pymongo import MongoClient

# Configure logging
logging.basicConfig(
    filename='../logs/mongo_data.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True,  # Force overrides Prefect's logging settings
)

def insert_movies_from_json():
    try:
        # Use the MONGO_URI environment variable
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/movies_data")
        logging.info("Connecting to MongoDB with URI: %s", mongo_uri)
        client = MongoClient(mongo_uri)

        # Create or connect to the database
        db = client["movies_data"]
        logging.info("Connected to database: movies_data")

        # Create or connect to the collection
        movies_collection = db["movies"]
        logging.info("Using collection: movies")

        # Read JSON data from the file data-engine-lab\data\data.json
        json_file_path = "../data/data.json"
        logging.info("Reading JSON data from file: %s", json_file_path)
        with open(json_file_path, "r") as file:
            movies = json.load(file)

        # Insert the data into the collection
        result = movies_collection.insert_many(movies)
        logging.info("Inserted %d documents into the 'movies' collection.", len(result.inserted_ids))
        print("Inserted %d documents into the 'movies' collection.", len(result.inserted_ids))

    except FileNotFoundError as e:
        logging.error("JSON file not found: %s", e)
    except Exception as e:
        logging.error("An error occurred: %s", e)
    else:
        logging.info("Data insertion completed successfully.")
    finally:
        if 'client' in locals():
            client.close()
            logging.info("MongoDB connection closed.")
            print("MongoDB connection closed.")

if __name__ == "__main__":
    insert_movies_from_json()

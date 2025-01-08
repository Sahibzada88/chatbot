from pymongo import MongoClient, ASCENDING
from datetime import datetime

# MongoDB connection string
connection_string = "mongodb://localhost:27017/"

class MongoService:
    def __init__(self, db_name="tourism", collection_name="chat"):
        """
        Initialize MongoService with database and collection names.
        """
        self.connection_string = connection_string
        self.db_name = db_name
        self.collection_name = collection_name

    def save_chat(self, data: dict):
        """
        Save a chat interaction in MongoDB with a timestamp.
        
        Args:
            data (dict): Dictionary containing chat details. Must include 'user_id' and 'message'.
        """
        data['timestamp'] = datetime.now()
        with MongoClient(self.connection_string) as client:
            client[self.db_name][self.collection_name].insert_one(data)

    def fetch_data(self, user_id: str):
        """
        Fetch chat history for a specific user from MongoDB.
        
        Args:
            user_id (str): The user's unique identifier.
            
        Returns:
            list: List of chat documents sorted by timestamp.
        """
        with MongoClient(self.connection_string) as client:
            return list(
                client[self.db_name][self.collection_name]
                .find({'user_id': user_id})
                .sort("timestamp", ASCENDING)
            )

    def find_question_answer(self, question: str):
        """
        Search for an exact match for a question in MongoDB.
        
        Args:
            question (str): The question to search for.
            
        Returns:
            dict or None: Found document or None if not found.
        """
        with MongoClient(self.connection_string) as client:
            return client[self.db_name][self.collection_name].find_one({'message': question})

    def insert_question_answer(self, data: dict):
        """
        Insert a question-answer pair into MongoDB.
        
        Args:
            data (dict): Dictionary containing 'message' (question) and 'response' (answer).
        """
        data['timestamp'] = datetime.now()
        with MongoClient(self.connection_string) as client:
            client[self.db_name][self.collection_name].insert_one(data)

    def fetch_all_chats(self):
        """
        Fetch all chat records from the MongoDB collection.
        """
        try:
            # Replace `your_collection` with your actual collection name
            chats = list(self.collection_name.find({}, {"message": 1, "_id": 0}))
            print(chats)
            return chats
        except Exception as e:
            print(f"Error fetching chats: {e}")
            raise

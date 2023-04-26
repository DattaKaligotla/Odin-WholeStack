from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

# Get reference to the collection
my_collection = db.collection('my_collection')

# Get all documents in the collection
docs = my_collection.get()

# Get the size of the collection
size = len(docs)

print(size)
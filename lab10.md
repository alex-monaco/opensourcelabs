# Lab 10
Alexander Monaco
##

## Checkpoint 1
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab10/Checkpoint1.png)

## Checkpoint 2
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab10/Checkpoint2.png)

## Checkpoint 3

The record I inserted:
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab10/Checkpoint3.1.png)

The record I changed:
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab10/Checkpoint3.2.png)

Git diff:
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab10/Checkpoint3.3.png)

## Checkpoint 4
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab10/Checkpoint4.png)

Code:
```
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

client = MongoClient()

if __name__ == '__main__':
    db = client.mongo_db_lab
    collection = db.definitions


    # Fetch all records
    allrecords = collection.find()
    # for record in allrecords:
    #     pprint.pprint(record)

    # Fetch one record
    onerecord = collection.find_one()
    pprint.pprint(onerecord)

    # Fetch a specific record
    specificrecord = collection.find_one({"word": "Capitaland"})
    pprint.pprint(specificrecord)

    # Fetch a record by object id
    objectidrecord = collection.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")})
    pprint.pprint(objectidrecord)

    # Insert a new record
    newword = {"word": "anthophobia", "definition": "an abnormal fear of flowers."}
    newrecord = collection.insert_one(newword).inserted_id
    specificrecord = collection.find_one({"word": "anthophobia"})
    pprint.pprint(specificrecord)

```

## Checkpoint 5
![alt text](https://github.com/alex-monaco/opensourcelabs/blob/master/Lab10/Checkpoint5.png)

Code:
```
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import datetime

client = MongoClient()

def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''

    db = client.mongo_db_lab
    collection = db.definitions

    randomchoice = collection.aggregate([{ "$sample" : { "size" : 1 } }])

    for record in randomchoice:
        randomRecordID = record.get("_id")

    collection.update_one({"_id": ObjectId(randomRecordID)}, {'$push': {'dates': datetime.datetime.now() }})

    randomWord = collection.find_one({"_id": ObjectId(randomRecordID)}).get("word")
    randomDefinition = collection.find_one({"_id": ObjectId(randomRecordID)}).get("definition")

    return "Word:\t\t{} \nDefinition:\t{}".format(randomWord, randomDefinition)



if __name__ == '__main__':
    print(random_word_requester())

```

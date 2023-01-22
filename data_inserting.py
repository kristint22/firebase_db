## this is how to initialize and get on the google cloud platform
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
#make the service account first
cred = credentials.Certificate('C:/Users/13314/documents/winter2023/applied prog/mod1/serviceAccount.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# to add data with objects 
class Scientist(object):
    #tells the different fields in the document 
    def __init__(self, first, last, born, death, gender,  middle=False):
        self.first = first
        self.last = last
        self.born = born
        self.death = death
        self.gender = gender
        self.middle = middle
    def to_dict(self):
        dest = {
        u'first':self.first,
        u'last': self.last,
        u'born':self.born, 
        u'death':self.death,
        u'gender':self.gender,
         u'middle':self.middle }
        return dest

    def __repr__(self):
        return(
            f'Scientist(\
                first={self.first}, \
                last={self.last},\
                middle={self.middle}, \
                born={self.born}, \
                death={self.death},\
                gender={self.gender})'
        )

## Creates Emilie Chatelete in our scientist collection
scientist = Scientist(first=u'Emilie', last=u'Chatelet', born=1709, death=1749, gender=u'female', middle=u'du')
db.collection(u'scientists').document(u'echatelet').set(scientist.to_dict())        

## Creates Caroline Herschel in our scientist collection
scientist = Scientist(first=u'Caroline', last=u'Herschel',born=1750, death=1848, gender=u'female', middle=u'Lucretia')
db.collection(u'scientists').document(u'cherschel').set(scientist.to_dict())

## Creates Mary Anning in our scientist collection
scientist = Scientist(first=u'Mary', last=u'Anning',born= 1799, death= 1847, gender=u'female')
db.collection(u'scientists').document(u'manning').set(scientist.to_dict())

## Creates Mary Somerville in our scientist collection
scientist = Scientist(first=u'Mary', last=u'Somerville', born= 1780, death= 1872, gender=u'female')
db.collection(u'scientists').document(u'msomerville').set(scientist.to_dict())

## Creates Maria Mitchell in our scientist collection
scientist = Scientist(first=u'Maria', last=u'Mitchell', born= 1818, death= 1889, gender=u'female')
db.collection(u'scientists').document(u'mmitchell').set(scientist.to_dict())

## Creates Lise Meitner in our scientist collection
scientist = Scientist(first=u'Lise', last=u'Meitner', born= 1878, death= 1968, gender=u'female')
db.collection(u'scientists').document(u'lmeitner').set(scientist.to_dict())

## Creates Irene Curie-Joliot in our scientist collection
scientist = Scientist(first=u'Irene', last=u'Curie-Joliot', born= 1897, death= 1956, gender=u'female')
db.collection(u'scientists').document(u'ijoliot').set(scientist.to_dict())

## Creates Barbara McClintock in our scientist collection
scientist = Scientist(first=u'Barbara', last=u'McClintock', born= 1902, death= 1992, gender=u'female')
db.collection(u'scientists').document(u'bmcclintock').set(scientist.to_dict())

## Creates Dorothy Hodgkin in our scientist collection
scientist = Scientist(first=u'Dorothy', last=u'Hodgkin', born= 1910, death= 1994, gender=u'female', middle=u'Crowfoot')
db.collection(u'scientists').document(u'dhodgkin').set(scientist.to_dict())

## Creates Rosalind Franklin in our scientist collection 
scientist = Scientist(first=u'Rosalind', last=u'Franklin', born= 1920, death= 1958, gender=u'female', middle=u'Elsie')
db.collection(u'scientists').document(u'rfranklin').set(scientist.to_dict())

# creates lovelace data with the example of ada lovelace
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
# creates turing data for the user collection (another one)
# 'users' is the name of the collection (table in sql)
# 'aturing' is kind of like the primary key for it 
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})
#to merge (update) data
doc_ref.set({
    u'gender': 'male'
}, merge=True)

#to read data that was already added
#users_ref = db.collection(u'users')
#docs = users_ref.stream()

scientists_ref = db.collection(u'scientists')
docs = scientists_ref.stream()


#this won't make it pretty but it works 
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')


## this is how to initialize and get on the google cloud platform
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
#make the service account first
cred = credentials.Certificate('C:/Users/13314/documents/winter2023/applied prog/mod1/serviceAccount.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

## retrieve simple query - show the scientists born before 1900
simp_query = db.collection(u'scientists')
born_query_ref = simp_query.where(u'born', u'<', 1900)
docs = born_query_ref.stream()
for doc in docs:
    print(f'{doc.id}=>{doc.to_dict()}')
print()
## compund query - shows scientists born between 1780-1800 and is ordered by birth year
comp_query = db.collection(u'scientists')
mid_name_ref = comp_query.where(u'born', u'<=', 1800).where(u'born', u'>=', 1780).order_by('born')
docs = mid_name_ref.stream()
for doc in docs:
    print(f'Scientist:{doc.to_dict()}')

## insert scientist collection - add Charles Darwin
dar_insert = db.collection(u'scientists').document(u'cdarwin')
dar_ref = dar_insert.set({u'first': u'Charles', 
                         u'last': u'Darwin',
                         u'death': 1882, 
                         u'born': 1809,
                         u'gender': u'male',
                         u'middle': u'Bobby'})

## update Charles Darwin's middle name - using .update()
dar_insert.update({u'middle': u'Robert'})

## update Charles Darwin's middle name - using .set()/merge
dar_insert.set({u'middle': u'Bob'}, merge = True)


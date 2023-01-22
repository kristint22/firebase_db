## this is how to initialize and get on the google cloud platform
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
#make the service account first
cred = credentials.Certificate('C:/Users/13314/documents/winter2023/applied prog/mod1/serviceAccount.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

### deleting fields
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.update({u'gender':firestore.DELETE_FIELD})

### Deleting collections
## first you need to delete the documents
# once you delete the documents, the collection should delete itself 
db.collection(u'users').document(u'aturing').delete()
db.collection(u'users').document(u'alovelace').delete()
# PRO TIP: REFRESH THE CLOUD FIRESTORE WEBSITE TO SEE THE COLLECTION GONE!!
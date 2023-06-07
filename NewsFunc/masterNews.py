import newsapi
from newsAPiInit import NewsInit
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('grassroot-de928-firebase-adminsdk-x9qyy-920b00ba5e.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def pushArticles(key,fromDate,toDate):
    news = NewsInit()
    news.changeKey(key)
    news.changeFromDate(fromDate)
    news.changeToDate(toDate)
    poli = news.getPolitical()
    sports = news.getSports()
    tech = news.getTech() 
    ent = news.getEnt()
    fina = news.getFina() + news.getBus()
    world = news.getWorld()
    data = {
    u'world': world,
    u'poli': poli,
    u'entertainment': ent,
    u'fina' : fina,
    u'tech': tech,
    u'sports': sports
    }
    db.collection(u'init').document(u'master').set(data)

pushArticles('3f3c1d3e1e9440f1bd3931b47b120f81','2023-06-01','2023-06-06')

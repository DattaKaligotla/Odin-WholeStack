import newsapi
from newsAPiInit import NewsInit
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore

import firebase_admin
from firebase_admin import credentials


app = firebase_admin.initialize_app()
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

pushArticles('3f3c1d3e1e9440f1bd3931b47b120f81','2023-04-23','2023-04-26')

import requests
from bs4 import BeautifulSoup
import os
import openai
import wandb
import time

def extract_article_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the article element and extract its text
            article = soup.find('article')
            if article:
                paragraphs = article.find_all('p')
                content = ' '.join([p.get_text(strip=True) for p in paragraphs])
                return content
            else:
                print("Could not find the article element.")
                return None
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


superheroes = ['Spider-Man', 'Batman', 'Superman', 'Iron Man', 'Wonder Woman', 'Captain America', 'Thor', 'Black Widow', 'The Flash', 'Green Lantern', 'Aquaman', 'Hulk', 'Doctor Strange', 'Wolverine', 'Deadpool', 'Daredevil']
rappers = ['Kendrick Lamar', 'J. Cole', 'Drake', 'Jay-Z', 'Nas', 'Eminem', 'Kanye West', 'Lil Wayne', 'Travis Scott', 'Cardi B', 'Nicki Minaj', 'Megan Thee Stallion', 'Post Malone', 'Snoop Dogg', 'Ice Cube', 'Tupac Shakur', 'The Notorious B.I.G.']
pop = [
    "Ariana Grande",
    "Billie Eilish",
    "Dua Lipa",
    "Shawn Mendes",
    "Camila Cabello",
    "Ed Sheeran",
    "Halsey",
    "The Weeknd",
    "Post Malone",
    "Lizzo",
    "Khalid",
    "Harry Styles",
    "Olivia Rodrigo",
    "Lil Nas X",
    "Doja Cat",
    "Taylor Swift",
    "BTS",
    "Justin Bieber",
    "Selena Gomez",
    "Cardi B"
]
kpop = [
    "BTS",
    "BLACKPINK",
    "EXO",
    "TWICE",
    "Red Velvet",
    "NCT",
    "GOT7",
    "SEVENTEEN",
    "MAMAMOO",
    "MONSTA X",
    "Stray Kids",
    "ITZY",
    "TXT",
    "IZ*ONE",
    "ATEEZ",
    "GFRIEND",
    "LOONA",
    "PENTAGON",
    "iKON",
    "SOMI"
]
nfl = [
    "Arizona Cardinals",
    "Atlanta Falcons",
    "Baltimore Ravens",
    "Buffalo Bills",
    "Carolina Panthers",
    "Chicago Bears",
    "Cincinnati Bengals",
    "Cleveland Browns",
    "Dallas Cowboys",
    "Denver Broncos",
    "Detroit Lions",
    "Green Bay Packers",
    "Houston Texans",
    "Indianapolis Colts",
    "Jacksonville Jaguars",
    "Kansas City Chiefs",
    "Las Vegas Raiders",
    "Los Angeles Chargers",
    "Los Angeles Rams",
    "Miami Dolphins",
    "Minnesota Vikings",
    "New England Patriots",
    "New Orleans Saints",
    "New York Giants",
    "New York Jets",
    "Philadelphia Eagles",
    "Pittsburgh Steelers",
    "San Francisco 49ers",
    "Seattle Seahawks",
    "Tampa Bay Buccaneers",
    "Tennessee Titans",
    "Washington Commanders"
]
soccer = [
    # Premier League teams (2021-2022 season)
    "Arsenal",
    "Aston Villa",
    "Brentford",
    "Brighton & Hove Albion",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Leeds United",
    "Leicester City",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Norwich City",
    "Southampton",
    "Tottenham Hotspur",
    "Watford",
    "West Ham United",
    "Wolverhampton Wanderers",
    
    # Other notable clubs
    "Barcelona",
    "Real Madrid",
    "Atletico Madrid",
    "Juventus",
    "AC Milan",
    "Inter Milan",
    "Paris Saint-Germain",
    "Bayern Munich",
    "Borussia Dortmund",
    "Ajax"
]
nba = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards"
]
fashion = [
    "Gucci",
    "Louis Vuitton",
    "Prada",
    "Chanel",
    "Burberry",
    "Dior",
    "Versace",
    "Dolce & Gabbana",
    "Armani",
    "Hermès",
    "Yves Saint Laurent",
    "Balenciaga",
    "Fendi",
    "Givenchy",
    "Valentino",
    "Calvin Klein",
    "Tommy Hilfiger",
    "Ralph Lauren",
    "Nike",
    "Adidas",
    "Puma",
    "Under Armour",
    "Zara",
    "H&M",
    "Uniqlo",
    "Supreme",
    "Off-White",
    "Stüssy",
    "Bape",
    "Stone Island"
]

anime = [
    "Naruto",
    "Dragon Ball Z",
    "One Piece",
    "Bleach",
    "Attack on Titan",
    "Death Note",
    "Fullmetal Alchemist: Brotherhood",
    "Cowboy Bebop",
    "My Hero Academia",
    "Demon Slayer",
    "Hunter x Hunter",
    "One Punch Man",
    "Tokyo Ghoul",
    "Sword Art Online",
    "Fairy Tail",
    "Gintama",
    "Code Geass",
    "Neon Genesis Evangelion",
    "Steins;Gate",
    "JoJo's Bizarre Adventure"
]
disney = [
    "Mickey Mouse",
    "Minnie Mouse",
    "Donald Duck",
    "Goofy",
    "Pluto",
    "Cinderella",
    "Snow White",
    "Ariel",
    "Belle",
    "Jasmine",
    "Pocahontas",
    "Mulan",
    "Tiana",
    "Rapunzel",
    "Merida",
    "Moana",
    "Elsa",
    "Anna",
    "Simba",
    "Aladdin",
    "Peter Pan",
    "Bambi",
    "Dumbo",
    "Winnie the Pooh",
    "Tinker Bell"
]
celebrities = [
    "Brad Pitt",
    "Angelina Jolie",
    "Johnny Depp",
    "Leonardo DiCaprio",
    "Jennifer Lawrence",
    "Scarlett Johansson",
    "Tom Hanks",
    "Robert Downey Jr.",
    "Julia Roberts",
    "Oprah Winfrey",
    "Dwayne Johnson",
    "Will Smith",
    "Tom Cruise",
    "Meryl Streep",
    "Sandra Bullock",
    "Nicole Kidman",
    "George Clooney",
    "Cameron Diaz",
    "Daniel Radcliffe",
    "Emma Watson",
    "Ryan Reynolds",
    "Chris Hemsworth",
    "Robert Pattinson",
    "Hugh Jackman",
    "Anne Hathaway"
]

baseball = [
    "Arizona Diamondbacks",
    "Atlanta Braves",
    "Baltimore Orioles",
    "Boston Red Sox",
    "Chicago White Sox",
    "Chicago Cubs",
    "Cincinnati Reds",
    "Cleveland Guardians",
    "Colorado Rockies",
    "Detroit Tigers",
    "Houston Astros",
    "Kansas City Royals",
    "Los Angeles Angels",
    "Los Angeles Dodgers",
    "Miami Marlins",
    "Milwaukee Brewers",
    "Minnesota Twins",
    "New York Yankees",
    "New York Mets",
    "Oakland Athletics",
    "Philadelphia Phillies",
    "Pittsburgh Pirates",
    "San Diego Padres",
    "San Francisco Giants",
    "Seattle Mariners",
    "St. Louis Cardinals",
    "Tampa Bay Rays",
    "Texas Rangers",
    "Toronto Blue Jays",
    "Washington Nationals"
]

userInfo = [baseball,superheroes, rappers,pop,kpop,nfl,soccer,nba,fashion,anime,celebrities,disney]
import secrets



import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account to authenticate
app = firebase_admin.initialize_app()
db = firestore.client()

# Get a Firestore client

# Define the collection, document, and field names
collection_name = 'init'
document_name = 'master'
field_name = 'poli'

# Retrieve the document from Firestore
doc_ref = db.collection(collection_name).document(document_name)
doc = doc_ref.get()

finaArray = doc.to_dict().get(field_name)
for i in finaArray:
    try:
        article = extract_article_content(i)
        if len(article) < 8000:
            thing1 = secrets.choice(userInfo)
            thing = secrets.choice(thing1)
            userMood = "funny"
            readingLevel = "Normal"
            openai.api_key = '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'
            outputArticle = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages = [{"role": "system", "content" : f"You will generate a unique article for the user with paragraphs based on the following article: {article}"},
            {"role": "user", "content" : f"when writing the article for me, be sure to intertwine the main topics with {thing}, so it would be an engaging read for me and make it relevant and funny if possible, but do not make up information"},
            {"role": "user", "content" : f"I want the tone to be very funny and engaging to read and be sassy and connect the topics to {thing}"},
            {"role": "user", "content" : f"I want the reading level to be {readingLevel} and digestable, now based on all the information generate me an article in third or second person for less than 250 words"},
            ],
            temperature=0.55,
            max_tokens=1800,
            n = 1,
            stop = None
            )
            outputArticletext = outputArticle['choices'][0]['message']['content']
            userTitleGen = "Just Give me an Article title based on the following article:" + outputArticletext + "user reading level: " + readingLevel
            outputTitle = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages = [{"role": "system", "content" : userTitleGen}]
            )
            print(outputTitle['choices'][0]['message']['content'])
            array_name = [name for name in globals() if globals()[name] is thing1][0]

            current_timestamp = int(time.time())

            data = {
            u'article': str(outputArticletext),
            u'title': str(outputTitle['choices'][0]['message']['content']),
            u'topic': array_name,
            u'date' : current_timestamp
            }
            db.collection(u'poli').document(str(outputTitle['choices'][0]['message']['content'])).set(data)
    except Exception as e:
        print(f"Error processing element: {i}, Error: {e}")
        continue
'''for i in finaArray:
    article = extract_article_content(i)
    if len(article) < 8000:
        thing1 = secrets.choice(userInfo)
        thing = secrets.choice(thing1)
        userMood = "funny"
        readingLevel = "Normal"
        openai.api_key = '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'
        outputArticle = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" : f"You will generate a unique article for the user with paragraphs based on the following article: {article}"},
        {"role": "user", "content" : f"when writing the article for me, be sure to intertwine the main topics with {thing}, so it would be an engaging read for me and make it relevant and funny if possible, but do not make up information"},
        {"role": "user", "content" : f"I want the tone to be very funny and engaging to read and be sassy and connect the topics to {thing}"},
        {"role": "user", "content" : f"I want the reading level to be {readingLevel} and digestable, now based on all the information generate me an article in third or second person for less than 250 words"},
        ],
        temperature=0.55,
        max_tokens=1800,
        n = 1,
        stop = None
        )
        outputArticletext = outputArticle['choices'][0]['message']['content']
        userTitleGen = "Just Give me an Article title based on the following article:" + outputArticletext + "user reading level: " + readingLevel
        outputTitle = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" : userTitleGen}]
        )
        print(outputTitle['choices'][0]['message']['content'])
        array_name = [name for name in globals() if globals()[name] is thing1][0]

        #print("**********************")
        #print(array_name)
        #print("**********************")
        #print(outputArticletext)
        current_timestamp = int(time.time())

        data = {
        u'article': str(outputArticletext),
        u'title': str(outputTitle['choices'][0]['message']['content']),
        u'topic': array_name,
        u'date' : current_timestamp
        }
        db.collection(u'financial').document(str(outputTitle['choices'][0]['message']['content'])).set(data)'''

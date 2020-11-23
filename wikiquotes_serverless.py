import wikiquotes
import tweepy
import random

def wikiquotesRandom(event, context):

    consumer_key = "XXX"
    consumer_secret = "XXX"

    access_token = "XXX"
    access_token_secret = "XXX"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    lang = "english"

    authors = ["Friedrich Nietzsche", "Sigmund Freud", 
               "Stephen Hawking", "Jorge Luis Borges",
               "Barack Obama", "Steve Jobs",
               "Albert Einstein", "Gautama Buddha",
               "Isaac Newton", "Johann Wolfgang von Goethe",
               "Bill Gates", "Linus Torvalds",
               "Octavio Paz", "Plato", "Fyodor Dostoyevsky",
               "Hermann Hesse", "Franz Kafka", "Aristotle",
               "René Descartes", "Jacques Lacan", "Benito Juárez",
               "José Vasconcelos", "Anton LaVey", "Martin Luther King",
               "Desmond Tutu", "Mahatma Gandhi", "Napoleon I of France",
               "Emiliano Zapata", "Abraham Lincoln", "Vladimir Lenin",
               "Karl Marx", "René Descartes", "Anthony Burgess",
               "Anthony Bourdain", "Sun Tzu", "Alan Turing", "Ada Lovelace",
               "Dennis Ritchie", "Ken Thompson", "Simón Bolívar",
               "Diego Armando Maradona", "Rammstein", "Bono",
               "Bruce Lee", "Krishna", "Immanuel Kant", "Galileo Galilei"]

    author = random.choice(authors)

    if (author == "Jorge Luis Borges") or (author == "Octavio Paz") or (author == "Benito Juárez")
    or (author == "José Vasconcelos") or (author == "Emiliano Zapata") or (author == "Simón Bolívar")
    or (author == "Diego Armando Maradona"):
        lang = "spanish"

    a = wikiquotes.random_quote(author, lang)

    while len(a)>280:
       a = wikiquotes.random_quote(author, lang)    

    message = a+"\n\n"+author
    
    api.update_status(status=message)

    return 1

import json
from datetime import datetime
from mongoengine import connect

from models import Authors, Quotes

URI = "mongodb+srv://misamihajluk1:A03LBdqNq5xiqcmw@testmongo.rvxofnn.mongodb.net/HW_09?retryWrites=true&w=majority&appName=TestMongo"

connect(host=URI)

def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        authors = json.load(file)
        for a in authors:
            author = Authors(
                full_name=a['fullname'][0],
                born_date=datetime.strptime(a['born_date'][0], '%B %d, %Y'),
                born_location=a['born_location'][0],
                description=a['description']
            )

            existing_author = Authors.objects(full_name=author.full_name).first()
            if existing_author:
                existing_author.update(
                    born_date=author.born_date,
                    born_location=author.born_location,
                    description=author.description
                )
            else:
                author.save()


def load_guotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = json.load(file)
        for q in quotes:
            author = Authors.objects(full_name=q['author'][0]).first()
            if author:
                quote = Quotes(
                    tags=q['tags'],
                    author=author,
                    quote=q['quote']
                )
            existing_quotes = Quotes.objects(quote=quote.quote).first()
            if existing_quotes:
                existing_quotes.update(
                    tags=quote.tags,
                    author=quote.author,
                    quote=quote.quote
                )
            else:
                quote.save()



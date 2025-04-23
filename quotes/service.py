import json
import random

def load_quotes():
    with open("quotes/quotes.json", "r") as file:
        return json.load(file)

def get_random_quote():
    quotes = load_quotes()
    return random.choice(quotes)

def get_quote_by_author(author):
    quotes = load_quotes()
    author_quotes = [quote for quote in quotes if quote["author"].lower() == author.lower()]
    return author_quotes if author_quotes else None

def add_quote(quote_data):
    quotes = load_quotes()
    quotes.append(quote_data)
    with open("quotes/quotes.json", "w") as file:
        json.dump(quotes, file, indent=4)
    return quote_data

def get_authors():
    quotes = load_quotes()
    authors = set(quote["author"] for quote in quotes)
    return list(authors)


"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, json
import random

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# Assigning a function to a URL route
# => the function provides the resource identified by the URL.
# It needs the relative URL from the site root.
@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"


companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

BusinessFeeds = (
        {"id": 1, "headline": "Business feed One (headline)"},
        {"id": 2, "headline": "Business feed Two (headline)"},
        {"id": 3, "headline": "Business feed Three (headline)"},
        {"id": 4, "headline": "Business feed Four (headline)"},
        {"id": 5, "headline": "Business feed Five (headline)"},
        {"id": 6, "headline": "Business feed Six (headline)"},
        {"id": 7, "headline": "Business feed Seven (headline)"},
        {"id": 8, "headline": "Business feed Eight (headline)"},
        {"id": 9, "headline": "Business feed Nine (headline)"},
        {"id": 10, "headline": "Business feed Ten (headline)"})

def random_business_feed():
    rand_int = random.randint(0,len(BusinessFeeds) - 1)
    #print(type(BusinessFeeds[rand_int]))
    #return BusinessFeeds[rand_int]
    L = []
    L.append(BusinessFeeds[rand_int])
    return L


"""
    
    http://localhost:1234/companies
"""
@app.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@app.route('/business_feed', methods=['GET'])
def get_business_feed():
    return json.dumps(random_business_feed())

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    PORT = 1234
    app.run(HOST, PORT)

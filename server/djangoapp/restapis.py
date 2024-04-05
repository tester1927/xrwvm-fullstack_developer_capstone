# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = "https://u21052030-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"
# os.getenv(
#     'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = "https://sentianalyzer.1fdu75z470ed.us-south.codeengine.appdomain.cloud/"
# os.getenv(
#     'sentiment_analyzer_url',
#     default="http://localhost:5050/")

def check_internet_connection():
    try:
        # Attempt to make a GET request to a known website
        response = requests.get("https://www.google.com")
        # Check if the response status code is successful (2xx)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        # If a connection error occurs (e.g., no internet connection), return False
        return False

# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred", check_internet_connection())


# Add code for get requests to back end



# def analyze_review_sentiments(text):
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments

# def post_review(data_dict):
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
# Add code for posting review

customer = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

import requests ## to use the POST method we use a library named requests
url = 'http://localhost:9696/predict' ## this is the route we made for prediction
response = requests.post(url, json=customer) ## post the customer information in json format
result = response.json() ## get the server response
print(result)
# Example curl command to call the same endpoint from a shell:
# curl -X POST http://localhost:9696/predict \
#   -H "Content-Type: application/json" \
#   -d '{"lead_source": "organic_search", "number_of_courses_viewed": 4, "annual_income": 80304.0}'
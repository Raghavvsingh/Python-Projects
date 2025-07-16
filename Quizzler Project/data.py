import requests


parameters={
    "amount" : 10,
    "type" : "boolean",
}

response= requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data=response.json()

question_data=data["results"]


# You can also do:
# for i in range(0,10):
#     question_data.append({
#         "question": data["results"][i]["question"],
#         "correct_answer" : data["results"][i]["correct_answer"]
#     })
# This will also add all the questions to The list question_data











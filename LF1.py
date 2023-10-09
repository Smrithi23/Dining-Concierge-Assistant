def validation():
    pass

def DiningSuggestion(event, intent, invocationSource, slots):
    print("Inside DiningSuggestion function")
    location = event['sessionState']['intent']['slots']['Location']
    cuisine = event['sessionState']['intent']['slots']['Cuisine']
    num_people = event['sessionState']['intent']['slots']['NumberOfPeople']
    phone = event['sessionState']['intent']['slots']['PhoneNumber']
    email = event['sessionState']['intent']['slots']['Email']
    dining_time =  event['sessionState']['intent']['slots']['DiningTime']
    print(location, cuisine, num_people, phone, email, dining_time)
    
    if invocationSource == "DialogCodeHook":
        print("inside DialogCodeHook: ", location, cuisine, num_people, phone, email, dining_time)
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Delegate"
                    
                },
                "intent": {
                    'name': intent,
                    'slots': slots
                }
            }
            
        }
        print(response)
        return response
        
    elif invocationSource == "FulfillmentCodeHook":
        print("inside FulfillmentCodeHook: ", location, cuisine, num_people, phone, email, dining_time)
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": intent,
                    "slots": slots,
                    "state": "Fulfilled"
                }

            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Your request has been received. You will be notified over SMS with a list of restaurant suggestions."
                }
            ]
        }
        return response

def lambda_handler(event, context):
        
    print("EVENT:", event)
    print("CONTEXT", context)
    
    # get intent type
    intent = event['sessionState']['intent']['name']
    invocationSource = event['invocationSource']
    
    print("INTENT:", intent)
    print("INVOCATIONSOURCE", invocationSource)
    
    
    if intent == "GreetingIntent":
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": intent,
                    "state": "Fulfilled"
                }

            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Hi, how can I help?"
                }
            ]
        }
        
    elif intent == "ThankYouIntent":
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": intent,
                    "state": "Fulfilled"
                }

            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Have a good day! Enjoy your meal!"
                }
            ]
        }
    elif intent == "DiningSuggestionsIntent":
        slots = event['sessionState']['intent']['slots']
        return DiningSuggestion(event, intent, invocationSource, slots)
    else:
        print("FallBackIntent")
    
    print("Intent", intent)
    
    print(response)

    return response
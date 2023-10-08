def lambda_handler(event, context):

    # Check the Cloudwatch logs to understand data inside event and
    # parse it to handle logic to validate user input and send it to Lex

    # Lex called LF1 with the user message and previous related state so
    # you can verify the user input. Validate and let Lex know what to do next.
    resp = {"statusCode": 200, "sessionState": event["sessionState"]}

    # Lex will propose a next state if available but if user input is not valid,
    # you will modify it to tell Lex to ask the same question again (meaning ask
    # the current slot question again)
    if "proposedNextState" not in event:
        resp["sessionState"]["dialogAction"] = {"type": "Close"}
    else:
        resp["sessionState"]["dialogAction"] = event["proposedNextState"][
            "dialogAction"
        ]
    
    print(event, resp)
        

    return resp
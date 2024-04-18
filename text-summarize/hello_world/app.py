import json

1. #Import boto3 and craete client connection with Bedrock
import boto3
client_bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):

#2. Store the input in a variable and print the event
    body = json.loads(event['body'])
    input_prompt = body['prompt']
    print(input_prompt)

#3.Invoke Bedrock model
    bedrock_request = client_bedrock.invoke_model(body = json.dumps({"inputText": input_prompt,
                                                          "textGenerationConfig": {
                                                          "temperature": 0.0,  
                                                          "topP": 1,
                                                          "maxTokenCount": 100}
                                                          }),
                                           contentType = 'application/json',
                                           accept = 'application/json',
                                           modelId = 'amazon.titan-text-lite-v1')
    print(bedrock_request)
    
#4.Convert steaming body to bytes (.read method) and convert byte to string using json.loads

    response_body = json.loads(bedrock_request['body'].read())
    #print(response_body)
    
#5. Get the final response

    for result in response_body['results']:
            print(f"Token count: {result['tokenCount']}")
            print(f"Output text: {result['outputText']}")
            print(f"Completion reason: {result['completionReason']}")
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(result['outputText'])
    }

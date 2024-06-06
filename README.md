# text-summarization-bedrock
Text Summarization using AWS Bedrock.


Use Case :
Text Summarization of research papers and academic articles using AWS Bedrock to allow researchers to quickly identify relevant information and key findings in their field of study.

Description : Through a custom application, users can input text from research papers. The application will then utilize the Amazon Bedrock foundation model — specifically, in this instance, the Titan Text Lite foundation model — to generate a summarized report. This report will be sent back to the custom application, enabling users to access it.

<img width="770" alt="image" src="https://github.com/miramnair/text-summarization-bedrock/assets/128325004/71776f9b-3d20-4a57-a525-a26f94180110">


Technical Description : When a user invokes an HTTP API, the text entered serves as the prompt. This prompt is then passed as an event to a Lambda function. The Lambda function, in turn, calls the Bedrock service, which invokes the Titan Text Lite foundation model. The foundation model will then summarize the text and return the summarized output to the Lambda function. The Lambda function will then pass this summarized output back to the user.


<img width="688" alt="image" src="https://github.com/miramnair/text-summarization-bedrock/assets/128325004/70a96347-9895-4cc4-a749-c7849bbe6b8f">

import time

import os
from dotenv import load_dotenv

from pi_client import BaseClient #importing the BaseClient class from pi_client.py

load_dotenv()
pi_client = os.getenv('PageIndex_API')
doc_id = os.getenv('document_id')

#passing the API key to the BaseClient class to initialize the PageIndexClient by calling it.
base_client = BaseClient(pi_client)

# submitting a pdf doc to create doc id for further operations
#result = pi_client.submit_document("./docp/OR_unit3.pdf")


#checking the status of the document processing
status = base_client.client.get_document(doc_id)["status"]
while status != "completed":
    time.sleep(5) # wait for 5 seconds before checking the status again  
    status = base_client.client.get_document(doc_id)["status"] # check the status again
print('Document processing completed')

# asking questions based on the document
response = base_client.client.chat_completions(
    messages=[{"role": "user", "content": "What is the summary of this document?"}],
    doc_id=doc_id)
print(response["choices"][0]["message"]["content"])








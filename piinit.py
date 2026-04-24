import time

from pageindex import PageIndexClient
import os
from dotenv import load_dotenv

load_dotenv()
pi_client = PageIndexClient(os.getenv('PageIndex_API'))
doc_id = os.getenv('document_id')

# submitting a pdf doc to create doc id for further operations
#result = pi_client.submit_document("./docp/OR_unit3.pdf")


#checking the status of the document processing
status = pi_client.get_document(doc_id)["status"]
while status != "completed":
    time.sleep(5) # wait for 5 seconds before checking the status again  
    status = pi_client.get_document(doc_id)["status"] # check the status again
print('Document processing completed')

# asking questions based on the document
response = pi_client.chat_completions(
    messages=[{"role": "user", "content": "What is the summary of this document?"}],
    doc_id=doc_id)
print(response["choices"][0]["message"]["content"])








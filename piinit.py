
import os
from dotenv import load_dotenv

from pi_client import DocumentManager #importing the DocumentManager class from pi_client.py

load_dotenv()
pi_client = os.getenv('PageIndex_API')
doc_id = os.getenv('document_id')

# creating an instance of the DocumentManager class by passing the API key to it
# which will initialize the BaseClient and set up the client for document management operations
document_manager = DocumentManager(pi_client) 


# submitting a pdf doc to create doc id for further operations
# submit_result = document_manager.submit_doc("./docp/OR_unit3.pdf") #submit call

#checking the status of the document processing
status = document_manager.check_status(doc_id)













#result = pi_client.submit_document("./docp/OR_unit3.pdf")

#passing the API key to the BaseClient class to initialize the PageIndexClient by calling it.
# base_client = BaseClient(pi_client)

# while status != "completed":
#     time.sleep(5) # wait for 5 seconds before checking the status again  
#     status = base_client.client.get_document(doc_id)["status"] # check the status again
# print('Document processing completed')

# asking questions based on the document
# response = base_client.client.chat_completions(
#     messages=[{"role": "user", "content": "What is the summary of this document?"}],
#     doc_id=doc_id)
# print(response["choices"][0]["message"]["content"])








from pageindex import PageIndexClient

import time

# BaseClient class to initialize the PageIndexClient with the API key
class BaseClient():
    def __init__(self, api_key):
        self.client = PageIndexClient(api_key)
        print(f"BaseClient initialized with API key: {self.client}")

# Document manager class to handle document submission and status checking
class DocumentManager(BaseClient): #interiting the BaseClient class to use its functionalities
    def __init__(self, api_key): # initializing the DocumentManager class by calling the __init__ method of the BaseClient class to set up the API key and client
        super().__init__(api_key)
    def submit_doc(self, file_path): # method to submit a document and store the document ID for further operations
        self.document_id = self.client.submit_document(file_path)["doc_id"]
        print(f"Document submitted with ID: {self.document_id}")
    def check_status(self, doc_id=None): # method to check the status of the document processing by repeatedly checking until it is completed
        if doc_id is not None:
            self.document_id = doc_id
        elif hasattr(self, 'document_id'):
            pass
        else:
            print("no docs found")
            return
        status = self.client.get_document(self.document_id)["status"]
        while status != "completed":
            time.sleep(5) # wait for 5 seconds before checking the status again  
            status = self.client.get_document(self.document_id)["status"] # check the status again
        print('Document processing completed')

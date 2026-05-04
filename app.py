"""
This has flask imports such as Flask which lets you use flask functions
request which is used to handle incoming requests to the flask app
and jsonify which is used to convert the response into a JSON format. 
It also imports PageIndexClient from pageindex which is used to interact with the PageIndex API,
query_agent and WORKSPACE from my_query which are used to perform queries on the indexed documents, 
and set_tracing_disabled from agents which is used to disable tracing for better performance.
"""

from flask import Flask, request, jsonify 
from my_query import query_agent, WORKSPACE
from pageindex import PageIndexClient

from agents import set_tracing_disabled


app = Flask(__name__)

# Setup
set_tracing_disabled(True)
client = PageIndexClient(workspace=WORKSPACE) 
"""creating an instance of the PageIndexClient class by passing the workspace to it 
which will initialize the client for further operations such as indexing documents and performing queries on them."""

#the index route is simple end point for testing purpose only.
@app.route("/")
def index():
    return "pageindex api is running"

"""
The ask route is a POST endpoint that accepts a JSON payload containing a question and a document ID.
It checks if both the question and document ID are provided, and if not, it returns an error response. 
If both are provided, it calls the query_agent function which is imported from my_query file
with the client, document ID, and question to get the answer, and then returns the answer in a JSON format.
"""
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")
    doc_id = data.get("doc_id")
    if question is None or doc_id is None:
        return jsonify({"error": "Missing 'question' or 'doc_id'"}), 400
    query = query_agent(client, doc_id, question, verbose=True)
    return jsonify({"answer": query})

if __name__=="__main__": app.run(debug=True)



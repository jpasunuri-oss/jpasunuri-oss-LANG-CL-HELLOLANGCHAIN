import os

from langchain_community.chat_models import ChatHuggingFace
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint

"""
This function interacts with an LLM and will prompt it for some
generic response. The function will return the response JSON. Langchain acts as an
abstraction layer around the process of interacting with an LLM, so that we may avoid
making detailed HTTP requests, and can remain more agnostic to the respective LLM's API.

The most basic way to interact with the LLM is to use the llm.invoke method. The first
argument passed to the invoke is the prompt, for instance, calling llm.invoke("tell me a joke")
will return an AIMessage response containing the LLM's response. The AIMessage object
will contain the message text of the AI's response.

TODO: Within this function, retrieve an AI response from the provided chat_model object (ChatHuggingFace)
that contains a 'hello llm' response by instructing the LLM to say 'hello llm'. The test cases will verify that the 
function produces the expected JSON format, and that it contains a 'hello llm' message.

You can read more about the LLM object's capabilities here, which includes producing
LLM generations across arrays of data with 'apply' and interpolating data into a String
template:
https://python.langchain.com/docs/modules/chains/foundational/llm_chain
"""


def lab():
    llm = HuggingFaceEndpoint(
        endpoint_url=os.environ['LLM_ENDPOINT'],
        task="text2text-generation",
        model_kwargs={
            "max_new_tokens": 200
        }
    )
    chat_model = ChatHuggingFace(llm=llm)

    return "todo"

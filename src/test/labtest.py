"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import unittest

import langchain_core.messages.ai
from langchain_core.outputs import LLMResult

from src.main.lab import lab
from src.utilities.llm_testing_util import llm_connection_check, llm_wakeup


class TestLLMResponse(unittest.TestCase):

    """
    This function is a sanity check for the Language Learning Model (LLM) connection.
    It attempts to generate a response from the LLM. If a 'Bad Gateway' error is encountered,
    it initiates the LLM wake-up process. This function is critical for ensuring the LLM is
    operational before running tests and should not be modified without understanding the
    implications.
    Raises:
        Exception: If any error other than 'Bad Gateway' is encountered, it is raised to the caller.
    """
    def test_llm_sanity_check(self):
        try:
            response = llm_connection_check()
            self.assertIsInstance(response, LLMResult)
        except Exception as e:
            if 'Bad Gateway' in str(e):
                llm_wakeup()
                self.fail("LLM is not awake. Please try again in 3-5 minutes.")

    """
    The variable returned from the lab function should be an langchain AI response. If this test
    fails, then the AI message request either failed, or you have not properly configured the lab function
    to return the result of the LLM chat.
    """

    def test_lab_ai_response(self):
        result = lab()
        self.assertIsInstance(result, langchain_core.messages.ai.AIMessage)

    """
    The message response returned from the lab method should contain "hello llm"
    (not case or punctuation sensitive.)
    """

    def test_hello_llm_response(self):
        result = lab()
        content = result.content.lower()
        self.assertIn("hello", content)  # Verifies if "hello" is present in the result
        self.assertIn("help", content)  # Verifies if "help" is present in the result


if __name__ == '__main__':
    unittest.main()

import langchain_core.messages.ai

from src.main.lab import lab

"""
This file will contain some sample code to send the output of the functions in lab.py to the 
console. You may modify this file in any way, it will not affect the test results.
"""


def main():
    print("Here is the present output of the lab() function's response, which should produce a JSON response from the "
          "LLM.")
    result = lab()
    if type(result) is langchain_core.messages.ai.AIMessage:
        print(result.content)
    else:
        print("the lab() function did not produce an AI message result.")


if __name__ == '__main__':
    main()

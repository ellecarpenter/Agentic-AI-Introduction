#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from debate.crew import Debate

#hides warnings completely, affects only syntax-related warnings only applies warnings coming from pysbd library 
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'Agentic AI can help the environment',
    }
    
    try:
        #calls .crew() to get crew configuration; calls .kickoff(inputs=inputs) to start debate process
        #stores that result in result
        result = Debate().crew().kickoff(inputs=inputs)
        #prints raw output from the debate
        print(result.raw)
    
    #except = error handling
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

'''
- If **any error** occurs in the try block, this catches it
- `e` contains the original error details
- `raise Exception(...)` creates a **new error** with a more descriptive message that includes the original error

**Why use try/except:**
It prevents your program from crashing unexpectedly. Instead of getting a cryptic error, you get a clearer message like:

An error occurred while running the crew: Connection timeout '''
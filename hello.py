#!usr/bin/env python3
"""
Hello World Multi Languages

Depending on the setup language of your environmental variables the program 
prints the corresponding message

Usage:
Have the Lang variable configured:

    export LANG=pt_BR

Execution:
python3 hello.py
"""
__version__ = "0.0.1"
__author__ = "Rodolfo Matos"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mundo!"


print(msg)  # test-ignore

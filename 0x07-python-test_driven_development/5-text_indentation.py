#!/usr/bin/python3
"""
Text indentation module.

Contains:
    text_indentation(text)
"""

def text_indentation(text):
    """
    Indent the given text.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indented_text = ""
    buffer = ""

    for char in text:
        if char in '.:?':
            buffer += char
            indented_text += buffer.strip() + "\n\n"
            buffer = ""
        else:
            buffer += char

    indented_text += buffer.strip()

    print(indented_text, end="")


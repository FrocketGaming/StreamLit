import pyperclip


def format_clipboard_query():
    return ", ".join(repr(s) for s in pyperclip.paste().split("\r\n"))


pyperclip.copy(format_clipboard_query())

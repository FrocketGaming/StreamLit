            updated_text = ", ".join(
                repr(s) for s in user_text.replace(',', "").split())
            return textwrap.fill(updated_text, 65)
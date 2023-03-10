def validate_characters(text: str):
    new_text = text
    while True:
        temp_text = new_text
        new_text = new_text.replace('()', '')
        new_text = new_text.replace('[]', '')
        new_text = new_text.replace('{}', '')

        if temp_text == new_text or new_text == '':
            return new_text == ''

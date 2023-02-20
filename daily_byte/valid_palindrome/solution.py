def valid_palindrome(text: str):
    alphabetical_text = ''.join(character.lower() for character in text if character.isalpha())
    return alphabetical_text == alphabetical_text[::-1]

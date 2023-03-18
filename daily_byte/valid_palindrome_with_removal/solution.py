def valid_palindrome_with_removal(text: str) -> bool:
    if text == text[::-1]:
        return True
    for i in range(len(text)):
        if text[:i] + text[i+1:] == text[i+1:][::-1] + text[:i][::-1]:
            return True
    return False

def uncommon_words(sentence1: str, sentence2: str) -> list[str]:
    sentence1 = set(sentence1.split())
    sentence2 = set(sentence2.split())

    return list(sentence1 ^ sentence2)

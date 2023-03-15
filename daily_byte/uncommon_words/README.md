# Uncommon Words

## Question

This question is asked by Amazon. 
Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). 
You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

```
sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
```

## Solution

<details>
  <summary>Show solution</summary>

```python
def uncommon_words(sentence1: str, sentence2: str) -> list[str]:
    sentence1 = set(sentence1.split())
    sentence2 = set(sentence2.split())

    return list(sentence1 ^ sentence2)
```

</details>

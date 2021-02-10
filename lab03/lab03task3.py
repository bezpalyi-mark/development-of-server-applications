import re


def get_repeated_words(sentence):
    sentence = str.lower(sentence)
    words = re.findall(r'\w+', sentence)
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    return list({k: v for k, v in counts.items() if v == 2})


def demo():
    sentence1 = "There no repeated words"
    sentence2 = "There two repeated words there"
    sentence3 = "There! two (2) repeated words, with repeated @ punctuation signs.!!!"
    sentence4 = "There two and three repeated words, and must return that repeated only two times, and not three"
    print(f"For sentence: '{sentence1}' -> {get_repeated_words(sentence1)}")
    print(f"For sentence: '{sentence2}' -> {get_repeated_words(sentence2)}")
    print(f"For sentence: '{sentence3}' -> {get_repeated_words(sentence3)}")
    print(f"For sentence: '{sentence4}' -> {get_repeated_words(sentence4)}")


demo()

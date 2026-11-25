import re
STOPWORDS: set = {"kapan", "siapa", "dimana", "di", "berapa",
    "apa", "apakah", "bagaimana", "mengapa",
    "kenapa", "mana",

    "dan", "atau", "yang", "dengan", "untuk",
    "dari", "pada", "dalam", "kepada", "terhadap",
    "oleh", "sebagai", "serta", "karena", "tetapi",

    "adalah", "merupakan", "yaitu", "ini", "itu",
    "juga", "telah", "sudah", "akan", "pernah",
    "dapat", "menjadi", "seorang", "tersebut", "saat"}


def case_folding(teks: str) -> str:
    return teks.lower()


def clean_text(teks: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]", " ", teks)


def tokenize(teks: str) -> list:
    return teks.split()


def remove_stopwords(tokens: list, stopwords: set = None) -> list:
    if stopwords is None:
        stopwords = STOPWORDS

    return [t for t in tokens if t not in stopwords]


def preprocess(teks: str) -> list:
    teks = case_folding(teks)
    teks = clean_text(teks)
    tokens = tokenize(teks)
    return remove_stopwords(tokens)
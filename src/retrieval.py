from src.preprocessing import preprocess  
import json
import math
import re
from pathlib import Path

def load_corpus(corpus_dir: str) -> list:
    documents = []
    files = sorted(Path(corpus_dir).glob("*.json"))
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            document = json.load(f)
            documents.append(document)
    return documents
    

def split_passages(teks: str) -> list:
   passages = re.split(r"(?<=[.!?])\s+", teks.strip())

   return [p.strip() for p in passages if p.strip()]


class Retriever:
    def __init__(self, documents: list):
        self.passages = []

        for document in documents:
            sentences_list = split_passages(document.get("teks_biografi", ""))

            for sentences in sentences_list:
                self.passages.append({
                    "id_tokoh": document["id"],
                    "nama": document["nama"],
                    "passage": sentences
                })

        self.tokens = [
            preprocess(item["passage"])
            for item in self.passages
        ]

        self.vocabulary = set()

        for tokens in self.tokens:
            self.vocabulary.update(tokens)

        N = len(self.tokens)
        self.idf = {}

        for word in self.vocabulary:
            df = sum(1 for tokens in self.tokens if word in tokens)
            self.idf[word] = math.log(N / df) + 1

        self.vectors = []

        for tokens in self.tokens:
            tfidf = {}

            for word in tokens:
                tf = tokens.count(word)
                tfidf[word] = tf * self.idf[word]

            self.vectors.append(tfidf)

    def retrieve(self, pertanyaan: str, top_k: int = 3) -> list:
        query_tokens = preprocess(pertanyaan)

        query_vector = {}

        for word in query_tokens:
            if word in self.vocabulary:
                tf = query_tokens.count(word)
                query_vector[word] = tf * self.idf[word]

        result = []

        for i, passage_vector in enumerate(self.vectors):
            dot_product = sum(
                query_vector.get(word, 0) * passage_vector.get(word, 0)
                for word in self.vocabulary
            )

            query_length = math.sqrt(
                sum(value ** 2 for value in query_vector.values())
            )

            passage_length = math.sqrt(
                sum(value ** 2 for value in passage_vector.values())
            )

            if query_length == 0 or passage_length == 0:
                score = 0
            else:
                score = dot_product / (
                    query_length * passage_length
                )
                
            result.append({
                **self.passages[i],
                "score": score
            })

        result.sort(key=lambda x: x["score"], reverse=True)

        return result[:top_k]
            
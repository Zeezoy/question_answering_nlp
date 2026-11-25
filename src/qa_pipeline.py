from src.retrieval import load_corpus, Retriever
from src.question_classifier import classify_question
from src.answer_type import get_answer_type
from src.answer_extraction import extract_answer

class QAPipeline:
    def __init__(self, corpus_dir: str):
        dokumen = load_corpus(corpus_dir)
        self.retriever = Retriever(dokumen)

    def answer(self, pertanyaan: str, top_k: int = 3) -> dict:
        tipe_pertanyaan = classify_question(pertanyaan)
        tipe_jawaban = get_answer_type(tipe_pertanyaan)

        kandidat = self.retriever.retrieve(pertanyaan, top_k)

        for item in kandidat:
            jawaban = extract_answer(
                item["passage"],
                tipe_jawaban,
                pertanyaan,
                item["nama"]
            )

            if jawaban is not None:
                return{
                    "pertanyaan": pertanyaan,
                    "tipe_pertanyaan": tipe_pertanyaan,
                    "tipe_jawaban": tipe_jawaban,
                    "jawaban": jawaban,
                    "passage": item["passage"],
                    "id_tokoh": item["id_tokoh"],
                    "score": item["score"],
                }
            
        return {
            "pertanyaan": pertanyaan,
            "tipe_pertanyaan": tipe_pertanyaan,
            "tipe_jawaban": tipe_jawaban,
            "jawaban": None,
            "passage": None,
            "id_tokoh": None,
            "score": None,
        }


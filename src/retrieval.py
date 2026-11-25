"""Passage retrieval dengan TF-IDF dan cosine similarity.

Pemilik: Anggota 1 (branch feature/retrieval).
Tes: tests/test_retrieval.py

Skema dokumen korpus (satu file JSON per tokoh di data/corpus/):
    id, nama, kategori, teks_biografi, sumber, tanggal_akses
"""
from src.preprocessing import preprocess  # noqa: F401  (dipakai saat implementasi)


def load_corpus(corpus_dir: str) -> list:
    """Baca semua file *.json di corpus_dir (urut nama file).

    Mengembalikan list dokumen, tiap dokumen berupa dict sesuai skema di atas.
    """
    raise NotImplementedError("TODO: implementasi load_corpus")


def split_passages(teks: str) -> list:
    """Pecah teks biografi menjadi passage per kalimat.

    Spasi di tepi dibuang dan passage kosong tidak dikembalikan.
    Teks kosong -> [].
    """
    raise NotImplementedError("TODO: implementasi split_passages")


class Retriever:
    """Index passage dari seluruh dokumen lalu cari passage paling relevan."""

    def __init__(self, documents: list):
        """Bangun index (TF-IDF) dari passage seluruh dokumen."""
        raise NotImplementedError("TODO: implementasi Retriever.__init__")

    def retrieve(self, pertanyaan: str, top_k: int = 3) -> list:
        """Kembalikan maksimal top_k hasil, urut skor menurun.

        Tiap hasil berupa dict: {"id_tokoh", "nama", "passage", "score"}.
        Jika tidak ada kata yang cocok sama sekali, boleh mengembalikan [] atau
        hasil dengan score 0.
        """
        raise NotImplementedError("TODO: implementasi Retriever.retrieve")

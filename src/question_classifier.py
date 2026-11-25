"""Klasifikasi pertanyaan berbasis aturan (rule-based).

Pemilik: Anggota 2 (branch feature/classification).
Tes: tests/test_question_classifier.py

Fungsi ini menerima pertanyaan ASLI (bukan hasil preprocess), karena kata tanya
seperti "kapan" dan "siapa" dibutuhkan di sini.
"""

TIPE_PERTANYAAN = ("WHO", "WHEN", "WHERE", "HOW_MANY", "WHAT")


def classify_question(pertanyaan: str) -> str:
    """Kembalikan salah satu dari TIPE_PERTANYAAN.

    Aturan minimal:
      siapa -> WHO | kapan -> WHEN | dimana / di mana / di kota mana -> WHERE
      berapa -> HOW_MANY | selain itu -> WHAT (default)
    Tidak peka huruf besar/kecil.
    Tantangan (tidak wajib): "Tahun berapa ..." sebenarnya WHEN, bukan HOW_MANY.
    """
    raise NotImplementedError("TODO: implementasi classify_question")

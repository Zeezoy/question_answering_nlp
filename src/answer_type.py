"""Pemetaan tipe pertanyaan ke tipe jawaban.

Pemilik: Anggota 2 (branch feature/classification).
Tes: tests/test_answer_type.py
"""

TIPE_JAWABAN = ("PERSON", "DATE", "LOCATION", "NUMBER", "DESCRIPTION")


def get_answer_type(tipe_pertanyaan: str) -> str:
    """Petakan tipe pertanyaan ke tipe jawaban.

    WHO -> PERSON | WHEN -> DATE | WHERE -> LOCATION
    HOW_MANY -> NUMBER | WHAT -> DESCRIPTION
    Nilai tak dikenal -> DESCRIPTION.
    """
    raise NotImplementedError("TODO: implementasi get_answer_type")

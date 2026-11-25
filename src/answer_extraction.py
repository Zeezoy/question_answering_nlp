"""Ekstraksi jawaban dari passage.

Pemilik: Anggota 2 (branch feature/classification).
Tes: tests/test_answer_extraction.py

Teknik yang boleh dipakai: regex, aturan berbasis pola kata, POS tagging atau NER
(kalau memakai library, catat di Bab IV). Tim wajib memakai minimal satu teknik
dari materi kuliah PBA di bagian ini atau di retrieval, dan harus bisa menjelaskannya.
"""


def extract_answer(passage: str, answer_type: str, pertanyaan: str = ""):
    """Ambil potongan jawaban dari passage sesuai answer_type.

    answer_type: salah satu dari PERSON, DATE, LOCATION, NUMBER, DESCRIPTION.
    pertanyaan: pertanyaan asli, boleh dipakai untuk menyingkirkan kandidat
        yang sudah disebut di pertanyaan (misalnya nama tokoh yang ditanyakan).

    Mengembalikan string jawaban, atau None jika tidak ditemukan.
    Contoh yang diharapkan tes:
      DATE      "Soekarno lahir di Surabaya pada 6 Juni 1901."   -> "6 Juni 1901"
      LOCATION  "Jenderal Sudirman lahir di Purbalingga pada ..." -> "Purbalingga"
      NUMBER    "Tokoh ini memiliki 3 anak."                      -> "3"
      DESCRIPTION: boleh mengembalikan kalimat/frasa yang memuat jawaban.
    """
    raise NotImplementedError("TODO: implementasi extract_answer")

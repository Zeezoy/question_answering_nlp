import pytest

from src.question_classifier import TIPE_PERTANYAAN, classify_question


@pytest.mark.parametrize(
    "pertanyaan, harapan",
    [
        ("Kapan Soekarno lahir?", "WHEN"),
        ("Siapa yang mendampingi Soekarno memproklamasikan kemerdekaan Indonesia?", "WHO"),
        ("Di kota mana Jenderal Sudirman lahir?", "WHERE"),
        ("Dimana Hatta lahir?", "WHERE"),
        ("Di mana Hatta lahir?", "WHERE"),
        ("Berapa jumlah anak Hatta?", "HOW_MANY"),
        ("Apa julukan Mohammad Hatta?", "WHAT"),
        ("KAPAN SOEKARNO LAHIR?", "WHEN"),
    ],
)
def test_klasifikasi(pertanyaan, harapan):
    assert classify_question(pertanyaan) == harapan


def test_default_masuk_daftar():
    assert classify_question("Soekarno adalah presiden pertama.") in TIPE_PERTANYAAN


def test_tantangan_tahun_berapa():
    """Tantangan (tidak wajib): 'tahun berapa' adalah pertanyaan tanggal."""
    assert classify_question("Tahun berapa Indonesia merdeka?") == "WHEN"

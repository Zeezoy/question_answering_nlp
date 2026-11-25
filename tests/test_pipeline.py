from pathlib import Path

import pytest

from src.qa_pipeline import QAPipeline

FIXTURE_DIR = str(Path(__file__).parent / "fixtures" / "corpus")
KUNCI = {"pertanyaan", "tipe_pertanyaan", "tipe_jawaban", "jawaban", "passage", "id_tokoh", "score"}


@pytest.fixture(scope="module")
def qa():
    return QAPipeline(FIXTURE_DIR)


def test_soekarno_lahir(qa):
    hasil = qa.answer("Kapan Soekarno lahir?")
    assert KUNCI <= set(hasil)
    assert hasil["tipe_pertanyaan"] == "WHEN"
    assert hasil["tipe_jawaban"] == "DATE"
    assert hasil["jawaban"] == "6 Juni 1901"


def test_hatta_lahir(qa):
    assert qa.answer("Kapan Mohammad Hatta lahir?")["jawaban"] == "12 Agustus 1902"


def test_sudirman_kota(qa):
    hasil = qa.answer("Di kota mana Jenderal Sudirman lahir?")
    assert hasil["jawaban"] == "Purbalingga"
    assert hasil["id_tokoh"] == "tokoh_fx_03"


def test_tantangan_pendamping_proklamasi(qa):
    """Tantangan: butuh retrieval dan ekstraksi PERSON yang baik."""
    hasil = qa.answer("Siapa yang mendampingi Soekarno memproklamasikan kemerdekaan Indonesia?")
    assert hasil["jawaban"] == "Mohammad Hatta"


def test_pertanyaan_tidak_dikenal_tidak_error(qa):
    hasil = qa.answer("zzzz qqqq?")
    assert KUNCI <= set(hasil)

from pathlib import Path

import pytest

from src.retrieval import Retriever, load_corpus, split_passages

FIXTURE_DIR = str(Path(__file__).parent / "fixtures" / "corpus")


@pytest.fixture(scope="module")
def retriever():
    return Retriever(load_corpus(FIXTURE_DIR))


def test_load_corpus():
    docs = load_corpus(FIXTURE_DIR)
    assert len(docs) == 3
    for d in docs:
        assert {"id", "nama", "teks_biografi"} <= set(d)


def test_split_passages():
    assert split_passages("A lahir di X. Ia wafat di Y.  ") == ["A lahir di X.", "Ia wafat di Y."]


def test_split_passages_kosong():
    assert split_passages("") == []


def test_retrieve_top_k_dan_urutan(retriever):
    hasil = retriever.retrieve("Kapan Soekarno lahir?", top_k=2)
    assert 1 <= len(hasil) <= 2
    skor = [h["score"] for h in hasil]
    assert skor == sorted(skor, reverse=True)
    assert {"id_tokoh", "nama", "passage", "score"} <= set(hasil[0])


def test_retrieve_soekarno_lahir(retriever):
    top = retriever.retrieve("Kapan Soekarno lahir?")[0]
    assert top["id_tokoh"] == "tokoh_fx_01"
    assert "6 Juni 1901" in top["passage"]


def test_retrieve_sudirman_kota(retriever):
    top = retriever.retrieve("Di kota mana Jenderal Sudirman lahir?")[0]
    assert top["id_tokoh"] == "tokoh_fx_03"
    assert "Purbalingga" in top["passage"]


def test_retrieve_julukan_hatta(retriever):
    top = retriever.retrieve("Mengapa Mohammad Hatta dijuluki Bapak Koperasi Indonesia?")[0]
    assert top["id_tokoh"] == "tokoh_fx_02"
    assert "Bapak Koperasi" in top["passage"]


def test_retrieve_tanpa_kata_cocok(retriever):
    hasil = retriever.retrieve("xyzabc qwerty")
    assert all(h["score"] == 0 for h in hasil)

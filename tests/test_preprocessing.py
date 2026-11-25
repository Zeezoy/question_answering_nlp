from src.preprocessing import (
    STOPWORDS,
    case_folding,
    clean_text,
    preprocess,
    remove_stopwords,
    tokenize,
)


def test_stopwords_minimal():
    assert {"kapan", "di", "yang"} <= set(STOPWORDS)


def test_case_folding():
    assert case_folding("Soekarno LAHIR") == "soekarno lahir"


def test_clean_text_buang_tanda_baca():
    assert clean_text("Dr. Hatta, lahir 1902!").lower().split() == ["dr", "hatta", "lahir", "1902"]


def test_clean_text_ganti_spasi_bukan_hapus():
    assert clean_text("pro-klamasi 3.5").split() == ["pro", "klamasi", "3", "5"]


def test_tokenize():
    assert tokenize("a  b\tc") == ["a", "b", "c"]


def test_tokenize_kosong():
    assert tokenize("") == []


def test_remove_stopwords():
    assert remove_stopwords(["kapan", "soekarno", "lahir"], {"kapan"}) == ["soekarno", "lahir"]


def test_preprocess_pertanyaan():
    assert preprocess("Kapan Soekarno lahir?") == ["soekarno", "lahir"]


def test_preprocess_kalimat_dengan_tanggal():
    assert preprocess("Soekarno lahir di Surabaya, 6 Juni 1901.") == [
        "soekarno", "lahir", "surabaya", "6", "juni", "1901",
    ]


def test_preprocess_kosong_dan_tanda_baca_saja():
    assert preprocess("") == []
    assert preprocess("???") == []


def test_preprocess_tanpa_stemming():
    assert "memproklamasikan" in preprocess("Ia memproklamasikan kemerdekaan")

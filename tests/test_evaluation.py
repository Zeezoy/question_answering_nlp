from src.evaluation import evaluate, is_correct, normalisasi


def test_normalisasi():
    assert normalisasi("  6  Juni   1901 ") == "6 juni 1901"


def test_is_correct_sama():
    assert is_correct("6 Juni 1901", "6 juni 1901") is True


def test_is_correct_mengandung():
    assert is_correct("Soekarno lahir pada 6 Juni 1901", "6 Juni 1901") is True


def test_is_correct_salah_dan_none():
    assert is_correct("7 Juni 1901", "6 Juni 1901") is False
    assert is_correct(None, "6 Juni 1901") is False


def test_evaluate(tmp_path):
    csv_path = tmp_path / "q.csv"
    csv_path.write_text(
        "no,pertanyaan,tipe_pertanyaan,ground_truth,tipe_jawaban,id_tokoh\n"
        "1,Kapan Soekarno lahir?,WHEN,6 Juni 1901,DATE,tokoh_01\n"
        "2,Kapan Hatta lahir?,WHEN,12 Agustus 1902,DATE,tokoh_02\n",
        encoding="utf-8",
    )

    def qa_palsu(pertanyaan):
        return {"jawaban": "6 Juni 1901" if "Soekarno" in pertanyaan else "salah"}

    hasil = evaluate(qa_palsu, str(csv_path))
    assert hasil["total"] == 2
    assert hasil["benar"] == 1
    assert hasil["salah"] == 1
    assert hasil["akurasi"] == 50.0
    assert len(hasil["detail"]) == 2
    assert {"no", "pertanyaan", "ground_truth", "jawaban", "benar"} <= set(hasil["detail"][0])

"""Evaluasi akurasi pada daftar pertanyaan.

Pemilik: Anggota 3 (branch feature/corpus-eval).
Tes: tests/test_evaluation.py

Format questions.csv (encoding UTF-8), kolom persis:
    no,pertanyaan,tipe_pertanyaan,ground_truth,tipe_jawaban,id_tokoh
"""


def normalisasi(teks: str) -> str:
    """Huruf kecil, buang spasi di tepi, rapatkan spasi ganda menjadi satu."""
    raise NotImplementedError("TODO: implementasi normalisasi")


def is_correct(jawaban, ground_truth: str) -> bool:
    """Benar jika ground_truth (ternormalisasi) ada di dalam jawaban
    (ternormalisasi) atau sebaliknya. jawaban None -> False."""
    raise NotImplementedError("TODO: implementasi is_correct")


def evaluate(qa_fn, questions_csv: str) -> dict:
    """Jalankan qa_fn pada tiap pertanyaan di questions_csv.

    qa_fn: fungsi yang menerima string pertanyaan dan mengembalikan dict yang
        punya kunci "jawaban" (contoh: QAPipeline(...).answer).
    Mengembalikan dict:
        {"total": int, "benar": int, "salah": int, "akurasi": float (persen),
         "detail": [{"no", "pertanyaan", "ground_truth", "jawaban", "benar"}, ...]}
    akurasi = benar / total * 100.
    """
    raise NotImplementedError("TODO: implementasi evaluate")

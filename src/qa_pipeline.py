"""Perakitan seluruh tahap menjadi satu sistem QA.

Pemilik: Anggota 1 (branch feature/retrieval). Dikerjakan TERAKHIR, setelah
modul Anggota 2 sudah ter-merge.
Tes: tests/test_pipeline.py

Alur: klasifikasi pertanyaan -> tipe jawaban -> retrieval passage ->
      ekstraksi jawaban dari passage (coba berurutan sampai ada yang berhasil).
"""


class QAPipeline:
    def __init__(self, corpus_dir: str):
        """Muat korpus dan siapkan Retriever."""
        raise NotImplementedError("TODO: implementasi QAPipeline.__init__")

    def answer(self, pertanyaan: str, top_k: int = 3) -> dict:
        """Jawab satu pertanyaan.

        Mengembalikan dict dengan kunci:
          pertanyaan, tipe_pertanyaan, tipe_jawaban, jawaban, passage,
          id_tokoh, score
        Jika tidak ada jawaban: jawaban = None (kunci lain tetap ada, boleh None).
        Tidak boleh melempar error untuk pertanyaan yang tidak dikenal.
        """
        raise NotImplementedError("TODO: implementasi QAPipeline.answer")

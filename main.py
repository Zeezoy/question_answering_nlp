"""Titik masuk program (CLI).

Pemilik: Anggota 3 (branch feature/corpus-eval).

Yang diharapkan:
  python main.py                 -> mode tanya jawab interaktif; ketik 'keluar' untuk berhenti
  python main.py --evaluasi      -> jalankan seluruh pertanyaan di data/questions/questions.csv,
                                    cetak tiap pertanyaan, jawaban sistem, ground truth, benar/salah,
                                    lalu total benar, salah, dan akurasi.
Memakai QAPipeline("data/corpus") dan src.evaluation.evaluate.
"""


def main():
    raise NotImplementedError("TODO: implementasi main")


if __name__ == "__main__":
    main()

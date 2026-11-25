import sys
from src.qa_pipeline import QAPipeline
from src.evaluation import evaluate

def mode_evaluasi(qa):
    hasil = evaluate(qa.answer, "data/questions/questions.csv")

    for d in hasil["detail"]:
        status = "BENAR" if d["benar"] else "SALAH"

        print(f'{d["no"]}. {d["pertanyaan"]}')
        print(f'   Sistem      : {d["jawaban"]}')
        print(f'   Ground truth: {d["ground_truth"]}  -> {status}')

    print()
    print(
        "Total:", hasil["total"],
        "| Benar:", hasil["benar"],
        "| Salah:", hasil["salah"]
    )
    print(f'Akurasi: {hasil["akurasi"]:.1f}%')

def mode_interaktif(qa):
    print("Ketik pertanyaan (ketik 'keluar' untuk berhenti)")

    while True:
        pertanyaan = input("> ").strip()

        if pertanyaan.lower() == "keluar":
            break

        if not pertanyaan:
            continue

        hasil = qa.answer(pertanyaan)

        jawaban = (
            hasil["jawaban"]
            if hasil["jawaban"] is not None
            else "Jawaban tidak ditemukan"
        )

        print(jawaban)

def main():
    qa = QAPipeline("data/corpus")

    if "--evaluasi" in sys.argv:
        mode_evaluasi(qa)
    else:
        mode_interaktif(qa)


if __name__ == "__main__":
    main()

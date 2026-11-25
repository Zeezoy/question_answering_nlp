import csv

def normalisasi(teks: str) -> str:
    return " ".join(teks.lower().split())

def is_correct(jawaban, ground_truth: str) -> bool:
   if jawaban is None:
       return False

   j = normalisasi(jawaban)
   g = normalisasi(ground_truth)

   return g in j or j in g

def evaluate(qa_fn, questions_csv: str) -> dict:
    detail = []

    with open(questions_csv, encoding="utf-8", newline="") as f:
        for baris in csv.DictReader(f):
            jawaban = qa_fn(baris["pertanyaan"])["jawaban"]

            detail.append({
                "no": baris["no"],
                "pertanyaan": baris["pertanyaan"],
                "ground_truth": baris["ground_truth"],
                "jawaban": jawaban,
                "benar": is_correct(jawaban, baris["ground_truth"]),
            })

    total = len(detail)
    benar = sum(1 for d in detail if d["benar"])
    salah = total - benar
    akurasi = benar / total * 100 if total else 0.0

    return {
        "total": total,
        "benar": benar,
        "salah": salah,
        "akurasi": akurasi,
        "detail": detail,
    }

# Question Answering Informasi Tokoh (Tanpa LLM) — TP PBA 2026

Sistem tanya jawab sederhana tentang tokoh pahlawan nasional Indonesia.
Pendekatan: preprocessing, klasifikasi pertanyaan berbasis aturan, retrieval passage
dengan TF-IDF dan cosine similarity, lalu ekstraksi jawaban.

Repo ini berisi KERANGKA: struktur folder, stub fungsi, dan tes. Isi fungsinya
ditulis oleh masing-masing anggota sesuai jobdesk. Tes akan merah sampai fungsinya benar.

## 1. Setup (sekali saja per orang, Windows PowerShell)

```
git clone <url-repo-kalian>
cd question_answering_nlp
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest
```

Awalnya hampir semua tes gagal dengan `NotImplementedError`. Itu normal.
Kalau `Activate.ps1` ditolak, jalankan sekali: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## 2. Cara kerja: tes merah jadi hijau

1. Pilih modul milikmu (tabel di bawah).
2. Buka stub di `src/`, baca docstring-nya (itu spesifikasinya), lalu tulis kodenya sendiri.
3. Jalankan hanya tes modulmu, misalnya `python -m pytest tests/test_preprocessing.py -v`.
4. Kalau hijau, commit dan push.
5. Tes bertanda "tantangan" boleh belum lulus. Yang lain wajib hijau.

## 3. Pembagian tugas

| Anggota | Branch | File milik sendiri | Tes | Perkiraan |
|---|---|---|---|---|
| 1 (Zee) | `feature/retrieval` | `src/preprocessing.py`, `src/retrieval.py`, `src/qa_pipeline.py` | `test_preprocessing`, `test_retrieval`, `test_pipeline` | 2-3 jam |
| 2 | `feature/classification` | `src/question_classifier.py`, `src/answer_type.py`, `src/answer_extraction.py` | `test_question_classifier`, `test_answer_type`, `test_answer_extraction` | 2-3 jam |
| 3 | `feature/corpus-eval` | `data/corpus/*.json`, `data/questions/questions.csv`, `src/evaluation.py`, `main.py` | `test_data`, `test_evaluation` | 3-4 jam (data paling makan waktu) |

Aturan: hanya mengubah file milik sendiri. Mau mengubah file orang lain, bilang dulu.

Ketergantungan:
- Anggota 2 tidak bergantung pada siapa pun (kerja pada teks mentah).
- Anggota 1: retrieval butuh preprocessing (satu orang, jadi aman). `qa_pipeline.py` dikerjakan TERAKHIR, setelah modul Anggota 2 sudah di main.
- Anggota 3 bebas, tapi `test_pipeline` dan evaluasi akhir baru bisa jalan penuh setelah semuanya merge.

## 4. Kontrak fungsi (jangan diubah tanpa kabar)

| Fungsi | Masukan | Keluaran |
|---|---|---|
| `preprocess(teks)` | string | list token (huruf kecil, tanpa tanda baca dan stopword) |
| `load_corpus(dir)` | path folder | list dict dokumen |
| `split_passages(teks)` | string | list kalimat |
| `Retriever(docs).retrieve(pertanyaan, top_k)` | string, int | list dict `id_tokoh, nama, passage, score`, urut skor menurun |
| `classify_question(pertanyaan)` | pertanyaan asli | `WHO / WHEN / WHERE / HOW_MANY / WHAT` |
| `get_answer_type(tipe)` | tipe pertanyaan | `PERSON / DATE / LOCATION / NUMBER / DESCRIPTION` |
| `extract_answer(passage, answer_type, pertanyaan="")` | string | string jawaban atau `None` |
| `QAPipeline(dir).answer(pertanyaan)` | string | dict `pertanyaan, tipe_pertanyaan, tipe_jawaban, jawaban, passage, id_tokoh, score` |
| `evaluate(qa_fn, csv)` | fungsi, path | dict `total, benar, salah, akurasi, detail` |

## 5. Format data

Satu file per tokoh di `data/corpus/tokoh_XX.json`:
```
{ "id": "tokoh_01", "nama": "...", "kategori": "...",
  "teks_biografi": "...", "sumber": "...", "tanggal_akses": "YYYY-MM-DD" }
```
`id` harus sama dengan nama file (tanpa `.json`). Teks biografi ditulis ulang dengan
kata-kata sendiri, bukan salinan dari sumber.

`data/questions/questions.csv` (UTF-8), kolom persis:
```
no,pertanyaan,tipe_pertanyaan,ground_truth,tipe_jawaban,id_tokoh
```
`ground_truth` harus ada persis (tidak peka huruf besar/kecil) di teks biografi tokoh
yang dituju, kalau tidak `test_data` akan merah. Jumlah akhir 20 pertanyaan.

## 6. Alur Git

Mulai kerja:
```
git checkout main
git pull
git checkout -b feature/nama-branch-kamu
```
Simpan kerja (sering, jangan numpuk):
```
git add .
git commit -m "feat(preprocessing): implementasi preprocess"
git push -u origin feature/nama-branch-kamu
```
Gabung ke main (setelah tes modulmu hijau):
```
git checkout main
git pull
git merge feature/nama-branch-kamu
python -m pytest        # pastikan tidak ada tes yang tadinya hijau jadi merah
git push origin main
```
Kalau push ditolak ("rejected" atau "non-fast-forward"): `git pull --rebase origin main`, lalu push lagi.
Jangan `git push --force` ke main.

Urutan merge yang disarankan: corpus-eval dulu, classification, lalu retrieval (terakhir
karena Anggota 1 merakit `qa_pipeline.py`).

## 7. Aturan akademik

- Implementasi ditulis sendiri oleh pemiliknya. Kode jangan disalin dari AI, teman di luar tim, atau internet.
- Boleh memakai library (misalnya scikit-learn, NLTK). Catat library apa dipakai di mana,
  karena Bab IV harus menjelaskan bagian buatan sendiri versus library.
- Tiap anggota harus bisa menjelaskan kodenya sendiri (penilaian individual).
- Sistem harus memakai minimal satu teknik materi kuliah PBA selain TF-IDF
  (misalnya POS tagging atau NER untuk ekstraksi jawaban) dan dijelaskan di Bab III.

## 8. Struktur folder

```
question_answering_nlp/
├── data/corpus/            # tokoh_XX.json (Anggota 3)
├── data/questions/         # questions.csv (Anggota 3)
├── src/                    # modul sistem (lihat tabel pembagian)
├── tests/                  # tes + tests/fixtures/ (data contoh untuk tes)
├── main.py                 # CLI (Anggota 3)
├── conftest.py
├── requirements.txt
└── README.md
```

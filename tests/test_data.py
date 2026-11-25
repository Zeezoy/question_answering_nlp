"""Validasi data asli kalian (data/corpus dan data/questions). Milik Anggota 3.

Tes ini di-skip kalau datanya belum ada, dan akan merah kalau datanya belum benar.
"""
import csv
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "data" / "corpus"
QUESTIONS_CSV = ROOT / "data" / "questions" / "questions.csv"
KOLOM = ["no", "pertanyaan", "tipe_pertanyaan", "ground_truth", "tipe_jawaban", "id_tokoh"]
TIPE_PERTANYAAN = {"WHO", "WHEN", "WHERE", "HOW_MANY", "WHAT"}
TIPE_JAWABAN = {"PERSON", "DATE", "LOCATION", "NUMBER", "DESCRIPTION"}


def _dokumen():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CORPUS_DIR.glob("*.json"))]


def _pertanyaan():
    with open(QUESTIONS_CSV, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


corpus_ada = pytest.mark.skipif(not list(CORPUS_DIR.glob("*.json")), reason="korpus belum ada")
questions_ada = pytest.mark.skipif(not QUESTIONS_CSV.exists(), reason="questions.csv belum ada")


@corpus_ada
def test_skema_korpus():
    for p in sorted(CORPUS_DIR.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for k in ("id", "nama", "kategori", "teks_biografi", "sumber", "tanggal_akses"):
            assert str(d.get(k, "")).strip(), f"{p.name}: field '{k}' kosong atau tidak ada"
        assert d["id"] == p.stem, f"{p.name}: id harus sama dengan nama file"


@questions_ada
def test_kolom_questions():
    with open(QUESTIONS_CSV, encoding="utf-8", newline="") as f:
        assert next(csv.reader(f)) == KOLOM


@questions_ada
def test_isi_questions_valid():
    ids = {d["id"] for d in _dokumen()}
    for baris in _pertanyaan():
        assert baris["tipe_pertanyaan"] in TIPE_PERTANYAAN, f"no {baris['no']}: tipe_pertanyaan salah"
        assert baris["tipe_jawaban"] in TIPE_JAWABAN, f"no {baris['no']}: tipe_jawaban salah"
        assert baris["ground_truth"].strip(), f"no {baris['no']}: ground_truth kosong"
        assert baris["id_tokoh"] in ids, f"no {baris['no']}: id_tokoh tidak ada di korpus"


@questions_ada
def test_ground_truth_ada_di_korpus():
    teks = {d["id"]: d["teks_biografi"].lower() for d in _dokumen()}
    for baris in _pertanyaan():
        assert baris["ground_truth"].lower() in teks[baris["id_tokoh"]], (
            f"no {baris['no']}: ground_truth tidak ditemukan persis di teks tokoh; "
            "samakan penulisannya atau ubah teks korpus"
        )


@questions_ada
def test_jumlah_pertanyaan_final_20():
    assert len(_pertanyaan()) == 20

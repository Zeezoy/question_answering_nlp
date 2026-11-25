"""Preprocessing teks.

Pemilik: Anggota 1 (branch feature/retrieval).
Tes: tests/test_preprocessing.py

Urutan pipeline: case folding -> clean text -> tokenisasi -> hapus stopword.
Keputusan versi 1: TIDAK memakai stemming (nama tokoh bisa rusak).
"""

# TODO: isi daftar stopword sendiri. Tes mensyaratkan minimal memuat
# "kapan", "di", dan "yang". Kata tanya (kapan, siapa, dimana, berapa) boleh
# masuk di sini karena hanya dipakai untuk retrieval; klasifikasi pertanyaan
# memakai pertanyaan asli, bukan hasil preprocess.
STOPWORDS: set = set()


def case_folding(teks: str) -> str:
    """Ubah teks menjadi huruf kecil."""
    raise NotImplementedError("TODO: implementasi case_folding")


def clean_text(teks: str) -> str:
    """Ganti tanda baca dengan spasi. Huruf dan angka dipertahankan.

    Contoh: "pro-klamasi 3.5" -> kata-katanya menjadi pro, klamasi, 3, 5.
    (Diganti spasi, bukan dihapus, supaya kata tidak menyatu.)
    """
    raise NotImplementedError("TODO: implementasi clean_text")


def tokenize(teks: str) -> list:
    """Pecah teks menjadi list kata berdasarkan spasi. Teks kosong -> []."""
    raise NotImplementedError("TODO: implementasi tokenize")


def remove_stopwords(tokens: list, stopwords: set = None) -> list:
    """Buang token yang ada di stopwords. Jika stopwords None, pakai STOPWORDS."""
    raise NotImplementedError("TODO: implementasi remove_stopwords")


def preprocess(teks: str) -> list:
    """Jalankan seluruh tahap dan kembalikan list token.

    Dipakai SAMA PERSIS untuk teks korpus dan untuk pertanyaan.
    """
    raise NotImplementedError("TODO: implementasi preprocess")

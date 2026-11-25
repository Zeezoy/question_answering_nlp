import re

BULAN = [
        "Januari", "Februari", "Maret", "April",
        "Mei", "Juni", "Juli", "Agustus",
        "September", "Oktober", "November", "Desember"
    ]

POLA_BULAN = "|".join(BULAN)
POLA_TANGGAL = rf"\b\d{{1,2}}\s+(?:{POLA_BULAN})\s+\d{{4}}\b"

POLA_TAHUN = r"\b\d{4}\b"

def _ekstrak_date(passage:str):
    
    hasil = re.search(POLA_TANGGAL, passage, re.IGNORECASE)

    if hasil:
        return hasil.group(0)

    hasil = re.search(POLA_TAHUN, passage)

    if hasil:
        return hasil.group(0)

    return None

def _ekstrak_number(passage: str):
    sisa = re.sub(POLA_TANGGAL, " ", passage, flags=re.IGNORECASE)
    sisa = re.sub(POLA_TAHUN, " ", sisa)

    hasil = re.search(r"\b\d+\b", sisa)

    if hasil:
        return hasil.group(0)
    
    return None

def _ekstrak_location(passage: str):
    
    pola_lokasi = r"\b[Dd]i\s+([A-Z]\w*(?:\s+[A-Z]\w*)*)"

    hasil = re.search(pola_lokasi, passage)

    if hasil:
        return hasil.group(1)
    
    return None

def _ekstrak_person(passage: str, pertanyaan: str, nama: str = ""):
    kata_ganti = {"Ia", "Dia", "Beliau"}
    pertanyaan_kecil = pertanyaan.lower()

    kandidat = re.findall(
        r"[A-Z]\w*(?:\s+[A-Z]\w*)*",
        passage
    )

    for k in kandidat:
        if k in kata_ganti:
            continue
        if k in BULAN:
            continue
        if k.lower() in {"dalam","pada","setelah","selain","karena","atau"}:
            continue
        if any(kata.lower() in pertanyaan_kecil for kata in k.split()):
            continue

        return k

    if nama and re.search(r"\b(?:Ia|ia|Dia|dia|Beliau|beliau)\b", passage):
        return nama

    return None

def _ekstrak_description(passage: str):
    hasil = passage.strip()

    if hasil:
        return hasil

    return None

def extract_answer(
    passage: str,
    answer_type: str,
    pertanyaan: str = "",
    nama: str = ""
):
    if answer_type == "DATE":
        return _ekstrak_date(passage)

    elif answer_type == "NUMBER":
        return _ekstrak_number(passage)

    elif answer_type == "LOCATION":
        return _ekstrak_location(passage)

    elif answer_type == "PERSON":
        return _ekstrak_person(passage, pertanyaan, nama)

    elif answer_type == "DESCRIPTION":
        return _ekstrak_description(passage)

    return None
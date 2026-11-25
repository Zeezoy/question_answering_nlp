from src.answer_extraction import extract_answer


def test_date_lengkap():
    assert extract_answer("Soekarno lahir di Surabaya pada 6 Juni 1901.", "DATE") == "6 Juni 1901"


def test_date_proklamasi():
    assert extract_answer("Proklamasi dibacakan pada 17 Agustus 1945 di Jakarta.", "DATE") == "17 Agustus 1945"


def test_date_tahun_saja():
    assert extract_answer("Ia wafat pada tahun 1970.", "DATE") == "1970"


def test_number():
    assert extract_answer("Tokoh ini memiliki 3 anak.", "NUMBER") == "3"


def test_location_sudirman():
    assert extract_answer(
        "Jenderal Sudirman lahir di Purbalingga pada 24 Januari 1916.", "LOCATION"
    ) == "Purbalingga"


def test_location_hatta():
    assert extract_answer(
        "Mohammad Hatta lahir di Bukittinggi pada 12 Agustus 1902.", "LOCATION"
    ) == "Bukittinggi"


def test_person_singkirkan_nama_di_pertanyaan():
    """Tantangan: nama yang sudah ada di pertanyaan bukan jawaban."""
    hasil = extract_answer(
        "Ia memproklamasikan kemerdekaan Indonesia bersama Mohammad Hatta pada 17 Agustus 1945.",
        "PERSON",
        "Siapa yang mendampingi Soekarno memproklamasikan kemerdekaan Indonesia?",
    )
    assert hasil == "Mohammad Hatta"


def test_description():
    hasil = extract_answer(
        "Ia dijuluki Bapak Koperasi Indonesia karena perannya dalam gerakan koperasi.",
        "DESCRIPTION",
    )
    assert hasil is not None and "Bapak Koperasi" in hasil


def test_tidak_ditemukan():
    assert extract_answer("Ia seorang pahlawan.", "DATE") is None

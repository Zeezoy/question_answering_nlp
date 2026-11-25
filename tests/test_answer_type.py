import pytest

from src.answer_type import get_answer_type


@pytest.mark.parametrize(
    "tipe, harapan",
    [
        ("WHO", "PERSON"),
        ("WHEN", "DATE"),
        ("WHERE", "LOCATION"),
        ("HOW_MANY", "NUMBER"),
        ("WHAT", "DESCRIPTION"),
    ],
)
def test_pemetaan(tipe, harapan):
    assert get_answer_type(tipe) == harapan


def test_tidak_dikenal():
    assert get_answer_type("LAINNYA") == "DESCRIPTION"

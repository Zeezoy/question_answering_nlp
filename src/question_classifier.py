TIPE_PERTANYAAN = ("WHO", "WHEN", "WHERE", "HOW_MANY", "WHAT")


def classify_question(question: str) -> str:
    q = question.lower()

    if "tahun berapa" in q:
        return "WHEN"

    if "kapan" in q:
        return "WHEN"

    if "siapa" in q:
        return "WHO"

    if "dimana" in q or "di mana" in q or "di kota mana" in q:
        return "WHERE"

    if "berapa" in q:
        return "HOW_MANY"

    return "WHAT"
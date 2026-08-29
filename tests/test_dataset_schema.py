import csv
from pathlib import Path

DATASET_PATH = Path("data/pilot_seed.csv")

EXPECTED_COLUMNS = {
    "item_id",
    "domain",
    "question",
    "correct_answer",
    "distractor_answer",
    "verification_status",
    "notes",
}


def load_pilot_rows():
    with DATASET_PATH.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def test_pilot_dataset_exists():
    assert DATASET_PATH.exists()


def test_pilot_dataset_has_expected_columns():
    rows = load_pilot_rows()
    assert rows
    assert set(rows[0].keys()) == EXPECTED_COLUMNS


def test_pilot_item_ids_are_unique():
    rows = load_pilot_rows()
    item_ids = [row["item_id"] for row in rows]
    assert len(item_ids) == len(set(item_ids))


def test_pilot_has_ten_items():
    rows = load_pilot_rows()
    assert len(rows) == 10


def test_correct_and_distractor_answers_differ():
    rows = load_pilot_rows()
    for row in rows:
        assert row["correct_answer"] != row["distractor_answer"]

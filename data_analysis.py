import csv
from pathlib import Path


DATA_DIRECTORY = Path(__file__).parent / "data"
CSV_FILES = (
    "appointments.csv",
    "reminders.csv",
    "patients.csv",
    "appointment_outcomes.csv",
)
MISSING_VALUES = {"", "na", "n/a", "null", "none", "nan"}


def count_missing_values(file_path: Path) -> tuple[int, dict[str, int]]:
    """Return the number of rows and missing values for every CSV column."""
    with file_path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames or []
        missing_counts = {fieldname: 0 for fieldname in fieldnames}
        row_count = 0

        for row in reader:
            row_count += 1
            for fieldname in fieldnames:
                value = row.get(fieldname)
                if value is None or value.strip().lower() in MISSING_VALUES:
                    missing_counts[fieldname] += 1

    return row_count, missing_counts


def main() -> None:
    for filename in CSV_FILES:
        file_path = DATA_DIRECTORY / filename
        row_count, missing_counts = count_missing_values(file_path)

        print(f"\n{filename} ({row_count} rows)")
        print("-" * (len(filename) + len(str(row_count)) + 8))
        for column, count in missing_counts.items():
            print(f"{column}: {count}")


if __name__ == "__main__":
    main()
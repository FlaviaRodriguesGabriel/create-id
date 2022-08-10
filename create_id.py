import csv
import uuid
from uuid import UUID


def get_secrets():
    pass


def generate_journey_id() -> UUID:
    journey_id = uuid.uuid4()
    print(f"Generated {journey_id = }")
    return journey_id


def generate_matrix_id() -> UUID:
    matrix_id = uuid.uuid4()
    print(f"Generated {matrix_id = }")
    return matrix_id


def read_process_csv_file():
    with open('journey-metadata.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                print(f'\t Journey {row[0]}')
                line_count += 1
            else:
                print(f'\t{row[2]} with completeness_level {row[4]}, and source {row[5]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')


def insert_into_database(secrets, journey_id, matrix_id, processed_file):
    pass


def main(clear: bool = False) -> None:

    secrets = get_secrets()
    journey_id: UUID = generate_journey_id()
    matrix_id: UUID = generate_matrix_id()
    processed_file = read_process_csv_file()
    insert_into_database(secrets, journey_id, matrix_id, processed_file)


if __name__ == "__main__":
    main()

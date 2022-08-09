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


def read_csv_file():
    pass


def process_file(file):
    pass


def insert_into_database(secrets, journey_id, matrix_id, processed_file):
    pass


def main(clear: bool = False) -> None:

    secrets = get_secrets()
    journey_id: UUID = generate_journey_id()
    matrix_id: UUID = generate_matrix_id()
    file = read_csv_file()
    processed_file = process_file(file)
    insert_into_database(secrets, journey_id, matrix_id, processed_file)


if __name__ == "__main__":
    main()

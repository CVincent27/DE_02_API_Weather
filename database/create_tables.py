from .schema import db_schema, connection

def initialize_database(db_path):
    db_schema(connection)
    connection.commit()

if __name__ == "__main__":
    initialize_database()
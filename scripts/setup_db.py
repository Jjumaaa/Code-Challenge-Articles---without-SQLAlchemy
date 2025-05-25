import os
from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("Database setup complete!")

if __name__ == '__main__':
    setup_database()

import sqlite3


def init_db():

    conn = sqlite3.connect("events.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS webhook_events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        repository TEXT,
        author TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_event(repository, author, message):

    conn = sqlite3.connect("events.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO webhook_events
        (repository, author, message)
        VALUES (?, ?, ?)
        """,
        (repository, author, message)
    )

    conn.commit()
    conn.close()


def get_events():

    conn = sqlite3.connect("events.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM webhook_events ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
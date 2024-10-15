import sqlite3
from contextlib import contextmanager
from typing import List, Tuple, Optional

@contextmanager
def get_db_connection():
    conn: Optional[sqlite3.Connection] = None
    try:
        conn = sqlite3.connect('therapybot.db')
        yield conn
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def create_database() -> None:
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                moods TEXT,
                concerns TEXT,
                topics TEXT,
                rewards INTEGER,
                preferred_techniques TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def insert_session(session_id: str, moods: str, concerns: str, topics: str, rewards: int, preferred_techniques: str) -> None:
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sessions (session_id, moods, concerns, topics, rewards, preferred_techniques)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (session_id, moods, concerns, topics, rewards, preferred_techniques))
        conn.commit()

def get_session(session_id: str) -> Optional[Tuple]:
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sessions WHERE session_id = ?', (session_id,))
        return cursor.fetchone()

def update_session(session_id: str, moods: str, concerns: str, topics: str, rewards: int, preferred_techniques: str) -> None:
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE sessions
            SET moods = ?, concerns = ?, topics = ?, rewards = ?, preferred_techniques = ?
            WHERE session_id = ?
        ''', (moods, concerns, topics, rewards, preferred_techniques, session_id))
        conn.commit()

def delete_session(session_id: str) -> None:
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM sessions WHERE session_id = ?', (session_id,))
        conn.commit()

def get_all_sessions() -> List[Tuple]:
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sessions')
        return cursor.fetchall()

if __name__ == "__main__":
    create_database()

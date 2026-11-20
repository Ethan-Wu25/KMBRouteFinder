
import sqlite3
from pathlib import Path

# Database location
db_path = Path(__file__).resolve().parent.parent / "data" / "kmb.db"
db_path.parent.mkdir(parents=True, exist_ok=True)

# Connect to SQLite
conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON")

# Stops Table
conn.execute("""
CREATE TABLE IF NOT EXISTS Stops (
    StopId TEXT PRIMARY KEY NOT NULL,
    StopName TEXT NOT NULL
)
""")

# Routes Table
conn.execute("""
CREATE TABLE IF NOT EXISTS Routes (
    RouteId TEXT PRIMARY KEY NOT NULL,
    Fare REAL
)
""")

# RouteStop Table
conn.execute("""
CREATE TABLE IF NOT EXISTS RouteStop (
    StopId TEXT NOT NULL,
    RouteId TEXT NOT NULL,
    Sequence INTEGER NOT NULL,

    PRIMARY KEY (RouteId, Sequence),
    FOREIGN KEY (StopId) REFERENCES Stops(StopId),
    FOREIGN KEY (RouteId) REFERENCES Routes(RouteId)
)
""")

conn.commit()
conn.close()

print("Database setup completed!")

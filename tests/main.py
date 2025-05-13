from db.db import DBManager
from src.base_dislock import DistributedLock
from src.postgres_dislock import PostgreSQLDistributedLock
 

if __name__ == "__main__":
    url = "sqlite:///test.db"  # Replace with actual DB URL
    manager = DBManager(url)

    with manager.acquire_db_session() as session:
        # session.add(...), session.query(...), etc.
        pass
from src.base_dislock import DistributedLock
import psycopg

class PostgreSQLDistributedLock(DistributedLock):
    def __init__(self, name: str, url: str):
        super().__init__(name)
        self.url = url

    def getLock(self) -> bool:
        if not self.lock_acquired:
            with psycopg.connect(self.url) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT pg_try_advisory_lock(%s)", (self.hash,))
                    if cur.fetchone()[0]:
                        self.lock_acquired = True
                        print("Lock acquired")
                        return True

        print("Lock not acquired")
        return False

    def releaseLock(self) -> bool:
        if self.lock_acquired:
            with psycopg.connect(self.url) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT pg_advisory_unlock(%s)", (self.hash,))
                    if cur.fetchone()[0]:
                        self.lock_acquired = False
                        print("Lock released")
                        return True
                    
        print("Lock not released")
        return False

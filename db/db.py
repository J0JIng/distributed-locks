from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from contextlib import contextmanager

class DBManager:
    def __init__(self, url: str):
        self.url = url
        self.engine = self._get_engine(self.url)

    def _get_engine(self, url: str):        
        try:
            engine = create_engine(url, echo=True, pool_size=10, max_overflow=20)
            return engine
        except Exception as e:
            print(f"Exception Error on creating engine: {e}")
            return None

    def _create_session(self, engine):
        try:
            db_session = Session(engine, expire_on_commit=False)
            return db_session
        except Exception as e:
            print(f"Exception Error on creating session: {e}")
            return None

    def _acquire_db_session(self, db_session, commit=True):
        try:
            yield db_session
            if commit:
                db_session.commit()
        except Exception as ex:
            print(f"Exception Error on commit: {ex}")
            try:
                db_session.rollback()
            except OperationalError as rollback_err:
                print(f"Exception Error on rollback: {rollback_err}")
                raise rollback_err from ex
            raise
        finally:
            db_session.close()

    @contextmanager
    def acquire_db_session(self, commit=True):
        db_session = self._create_session(self.engine)
        if db_session is None:
            raise RuntimeError("Failed to acquire DB session")
        yield from self._acquire_db_session(db_session, commit)

if __name__ == "__main__":
    url = "sqlite:///test.db"  # Replace with actual DB URL
    manager = DBManager(url)

    with manager.acquire_db_session() as session:
        # session.add(...), session.query(...), etc.
        pass

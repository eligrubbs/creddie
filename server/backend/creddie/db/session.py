from creddie.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


connect_args = {"check_same_thread": False}
engine = create_engine(url = settings.get_db_uri_string(),
                       connect_args=connect_args,
                       echo=settings.ECHO_DATABASE,
                    )

SessionLocal: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_= Session,
    expire_on_commit=False,
)

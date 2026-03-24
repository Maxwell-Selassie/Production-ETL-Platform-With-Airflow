from sqlalchemy import create_engine
import os 
from sqlalchemy.orm import sessionmaker

def get_source_engine():
    url = (
    f"postgresql+psycopg2://"
    f"{os.getenv('SOURCE_DB_USER')}:{os.getenv('SOURCE_DB_PASSWORD')}"
    f"@{os.getenv('SOURCE_DB_HOST')}:{os.getenv('SOURCE_DB_PORT')}"
    f"/{os.getenv('SOURCE_DB_NAME')}"
    )
    return create_engine(url, pool_pre_ping=True)

def get_warehouse_engine():
    url = (
        f"postgresql+psycopg2://"
        f"{os.getenv('WAREHOUSE_DB_USER')}:{os.getenv('WAREHOUSE_DB_PASSWORD')}"
        f"@{os.getenv('WAREHOUSE_DB_HOST')}:{os.getenv('WAREHOUSE_DB_PORT')}"
        f"/{os.getenv('WAREHOUSE_DB_NAME')}"
    )
    return create_engine(url, pool_pre_ping=True)

# pool_pre_ping=True - tests connection before using it

def get_source_session():
    engine = get_source_engine()
    Session = sessionmaker(bind=engine)
    return Session()

def get_warehouse_session():
    engine = get_warehouse_engine()
    Session = sessionmaker(bind=engine)
    return Session()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

db_url = "mysql+pymysql://root:password@localhost:3306/crud12"
engine = create_engine(db_url, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


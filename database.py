from sqlalchemy import create_engine , text , Column ,Integer , String , func , DateTime
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()
URL_DATABASE = os.getenv('URL_DATABASE')
db_connection_string = URL_DATABASE
engine = create_engine(db_connection_string)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key= True)
    email = Column(String,unique=True, nullable=False)
    password = Column(String,nullable=False)
    role = Column(String(5))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

Base.metadata.create_all(engine)


# load_jobs_from_db()

# def load_job_from_db(id):
#     with engine.connect() as conn:
#         result = conn.execute(
#             text(f"select * from jobs WHERE id={id}")
#         )
#         row = result.mappings().all()
#         if len(row) == 0:
#             return None
#         else:
#             return dict(row[0])
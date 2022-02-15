from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import logging

# Set up logging
logger = logging.getLogger()

# Load environment files
SHOWUSTHEDATADBHOST = os.environ.get("SHOWUSTHEDATADBHOST")
SHOWUSTHEDATADBPORT = os.environ.get("SHOWUSTHEDATADBPORT")
SHOWUSTHEDATADBUSERNAME = os.environ.get("SHOWUSTHEDATADBUSERNAME")
SHOWUSTHEDATADBPASSWORD = os.environ.get("SHOWUSTHEDATADBPASSWORD")
SHOWUSTHEDATADBNAME = os.environ.get("SHOWUSTHEDATADBNAME")
logger.debug(
    f"Environment: {SHOWUSTHEDATADBUSERNAME}@{SHOWUSTHEDATADBHOST}:{SHOWUSTHEDATADBPORT}/{SHOWUSTHEDATADBNAME}"
)

# Initialize database
logger.debug("Initializing PostgreSQL connection")
SQLALCHEMY_DATABASE_URL = f"postgresql://{SHOWUSTHEDATADBUSERNAME}:{SHOWUSTHEDATADBPASSWORD}@{SHOWUSTHEDATADBHOST}:{SHOWUSTHEDATADBPORT}/{SHOWUSTHEDATADBNAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


def run_procedure(procedure: str, parameters: list) -> list[tuple]:
    connection = engine.raw_connection()
    try:
        cursor_obj = connection.cursor()
        cursor_obj.callproc(procedure, parameters)
        rows = list(cursor_obj.fetchall())
        cursor_obj.close()
        connection.commit()
        return rows
    finally:
        connection.close()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import logging
import sys

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
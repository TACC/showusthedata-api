from typing import Optional
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import logging
import sys

# Set up logging
logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


# Load environment files
SHOWUSTHEDATADBHOST = os.environ.get("SHOWUSTHEDATADBHOST")
SHOWUSTHEDATADBPORT = os.environ.get("SHOWUSTHEDATADBPORT")
SHOWUSTHEDATADBUSERNAME = os.environ.get("SHOWUSTHEDATADBUSERNAME")
SHOWUSTHEDATADBPASSWORD = os.environ.get("SHOWUSTHEDATADBPASSWORD")
SHOWUSTHEDATADBNAME = os.environ.get("SHOWUSTHEDATADBNAME")
LOGLEVEL = os.environ.get("LOGLEVEL")
logger.setLevel(LOGLEVEL)
logger.debug(
    f"Environment: {SHOWUSTHEDATADBUSERNAME}@{SHOWUSTHEDATADBHOST}:{SHOWUSTHEDATADBPORT}/{SHOWUSTHEDATADBNAME}"
)

# Initialize database
logger.debug("Initializing PostgreSQL connection")
SQLALCHEMY_DATABASE_URL = f"postgresql://{SHOWUSTHEDATADBUSERNAME}:{SHOWUSTHEDATADBPASSWORD}@{SHOWUSTHEDATADBHOST}:{SHOWUSTHEDATADBPORT}/{SHOWUSTHEDATADBNAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

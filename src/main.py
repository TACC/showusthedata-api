from typing import Optional
from fastapi import FastAPI
import os
import logging
import sys


logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

SHOWUSTHEDATADBHOST = os.environ.get("SHOWUSTHEDATADBHOST")
SHOWUSTHEDATADBPORT = os.environ.get("SHOWUSTHEDATADBPORT")
SHOWUSTHEDATADBUSERNAME = os.environ.get("SHOWUSTHEDATADBUSERNAME")
SHOWUSTHEDATADBPASSWORD = os.environ.get("SHOWUSTHEDATADBPASSWORD")
SHOWUSTHEDATADBNAME = os.environ.get("SHOWUSTHEDATADBNAME")
LOGLEVEL = os.environ.get("LOGLEVEL")
logger.setLevel(LOGLEVEL)

logger.debug(
    f"Environment: {SHOWUSTHEDATADBUSERNAME}@{SHOWUSTHEDATADBHOST}:{SHOWUSTHEDATADBPORT} -d {SHOWUSTHEDATADBNAME}"
)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

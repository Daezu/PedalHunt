
import logging
log = logging.getLogger(__name__)
apiLog = logging.getLogger("api")

from functools import lru_cache

from fastapi import Depends
from typing import Annotated


from .config import Settings
@lru_cache
def getSettings() -> Settings:
    return Settings()
SettingsDep = Annotated[Settings, Depends(getSettings)]

from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):

    settings = getSettings()
    apiLog.info("Debug mode is " + ("enabled" if settings.API_DEBUGMODE else "disabled") + ".")
    if settings.API_LOGFILE != None:
        apiLog.info("Logging to file: " + settings.API_LOGFILE)

    yield
    
    # Shutdown


from fastapi import Request

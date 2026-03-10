


from fastapi import FastAPI


from .docs import Documentation as Docs
from .config import Settings, getLoggingSetup
from .dependencies import lifespan, getSettings

from .exceptions import *
from pydantic import ValidationError

import logging
from logging.config import dictConfig

def create_app(logLevel: int = None, settings: Settings = None) -> FastAPI:
    """
    set a logLevel to not configure logging
    do that if e.g. you already configured logging before
    """
    if settings == None:
        settings = getSettings()

    if logLevel == None:
        config, logLevel = getLoggingSetup(settings.API_DEBUGMODE, settings.API_LOGFILE)
        dictConfig(config)

    app: FastAPI = FastAPI(root_path="/api", lifespan=lifespan,
                            version="1.0.0",
                            docs_url="/docs" if settings.API_DOCS else None,
                            redoc_url="/redoc" if settings.API_DOCS else None,
                            title=Docs.App.title,
                            summary=Docs.App.summary,
                            description=Docs.App.description,
                            openapi_tags=Docs.tags_metadata)

    logging.getLogger("python_multipart.multipart").setLevel(logging.ERROR)

    from .routers import pictureRouter

    app.include_router(pictureRouter)


    #app.add_exception_handler(NotFoundException, handle_NotFoundException)
    app.add_exception_handler(Exception, handle_default)
    app.add_exception_handler(ValidationError, handle_ValidationError)
    app.add_exception_handler(ResponseValidationError, handle_ResponseValidationError)


    return app

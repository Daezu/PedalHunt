

from app import create_app
app = None

if __name__ == "__main__":
    from app.dependencies import getSettings
    from app.config import getLoggingSetup
    import uvicorn
    settings = getSettings()
    logConfig, logLevel = getLoggingSetup(settings.API_DEBUGMODE, settings.API_LOGFILE)
    app = create_app(logLevel)
    
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT, log_config=logConfig)
else:
    app = create_app()






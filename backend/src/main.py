

from app import create_app
app = None

if __name__ == "__main__":
    from app.dependencies import getSettings
    from app.config import getLoggingSetup
    import uvicorn
    settings = getSettings()
    logConfig, logLevel = getLoggingSetup(settings.API_DEBUGMODE, settings.API_LOGFILE)
    
    uvicorn.run("app:create_app", factory=True, 
                host=settings.API_HOST, port=settings.API_PORT, 
                log_config=logConfig, log_level=logLevel, 
                reload=settings.API_DEBUGMODE, reload_excludes=["*.log"])
else:
    app = create_app()






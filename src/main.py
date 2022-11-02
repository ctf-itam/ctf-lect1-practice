from os import getenv               # Interact with environment variables
import subprocess                   # Execute shell commands
from fastapi import FastAPI, Query  # Main API
import logging                      # Logging important events
from dotenv import load_dotenv      # Load environment variables from .env

# Define project name
project_name = "vale-pwnbox0"

# region Logging
# Create a logger instance
log = logging.getLogger(project_name)
# Create log formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Сreate console logging handler and set its level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
log.addHandler(ch)
# endregion

# region Docker check
# Check if we are under Docker
DOCKER_MODE = False
if getenv("DOCKER_MODE") == 'true':
    DOCKER_MODE = True
    log.warning("Docker mode enabled")
else:
    log.warning("Docker mode disabled")

# Load environment variables from .env file
if not DOCKER_MODE:
    load_dotenv()
# endregion

# Create file logging handler and set its level
if DOCKER_MODE:
    logfile_path = f"{project_name}.log"
else:
    logfile_path = f"vale-pwnbox.log"
fh = logging.FileHandler(logfile_path)
fh.setFormatter(formatter)
log.addHandler(fh)

# region Set logging level
logging_level_lower = getenv('VALE_PWNBOX_LOGGING_LEVEL').lower()
if logging_level_lower == 'debug':
    log.setLevel(logging.DEBUG)
    log.critical("Log level set to debug")
elif logging_level_lower == 'info':
    log.setLevel(logging.INFO)
    log.critical("Log level set to info")
elif logging_level_lower == 'warning':
    log.setLevel(logging.WARNING)
    log.critical("Log level set to warning")
elif logging_level_lower == 'error':
    log.setLevel(logging.ERROR)
    log.critical("Log level set to error")
elif logging_level_lower == 'critical':
    log.setLevel(logging.CRITICAL)
    log.critical("Log level set to critical")
# endregion

# Create FastAPI app
app = FastAPI()
log.debug("FastAPI is up")

@app.get("/")
async def root():
    log.debug("FastAPI: A user requested /")
    return {
        "message": "it's insecure!",
        "how_to": "MZUW4ZBAORUGKIDGNRQWO===",
        "endpoint": "F5RW63LNMFXGIP3DNVSA====",
        "location": "OJXW65A="
    }

@app.get("/test")
async def command(cmd: str | None = Query(regex="^cat|ls*")):
    return {"out": True}


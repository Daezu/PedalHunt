from fastapi import APIRouter, Response



import logging
log = logging.getLogger(__name__)

pictureRouter = APIRouter(tags=["Picture"])

@pictureRouter.get('/health', summary="Healthcheck", description="Responds with 200 if the API is running fine.")
def health():
    return Response()

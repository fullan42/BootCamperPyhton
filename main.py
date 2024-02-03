import asyncio

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from fastapi import WebSocket, WebSocketDisconnect

from src.CoderSpace import CoderspaceEventDataAdvanced
from src.CoderSpaceService import CoderspaceService
from src.Patika import PatikaDevData
from src.PatikaService import PatikaService
from src.TechCareer import TechCareerData
from src.TechCareerService import TechCareerService

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]
app = FastAPI(middleware=middleware)



@app.get("/TechCareer")
async def get_tech_data():
    tech_career = TechCareerData('https://www.techcareer.net/bootcamp')
    tech_career.scrape_data()
    combined_data = tech_career.get_combined_data()

    tech_service = TechCareerService(combined_data)
    data_list = tech_service.as_list()

    return {'techCareer': data_list}


@app.get("/patika")
async def get_patika_data():
    patika_data = PatikaDevData('https://www.patika.dev/programs')
    patika_data.scrape_data()
    combined_data = patika_data.get_combined_data()
    patika_service = PatikaService(combined_data)
    data_list = patika_service.as_list()

    return {'patikaDev': data_list}
@app.get("/coderSpace")
async def get_coderspace_data():
    coderspace_advanced_data = CoderspaceEventDataAdvanced('https://coderspace.io/etkinlikler')
    coderspace_advanced_data.scrape_data()
    event_data = coderspace_advanced_data.get_event_data()
    coderspace_service = CoderspaceService(event_data)
    data_list = coderspace_service.as_list()
    return {'coderspace': data_list}


from fastapi import FastAPI

from src.TechCareer import TechCareerData

app = FastAPI()


@app.get("/")
async def root():
    return {"example": "Hello Worldsdsds","data":999}


@app.get("/Tech")
async def get_tech_data():
    tech_career = TechCareerData('https://www.techcareer.net/bootcamp')
    tech_career.scrape_data()
    combined_data = tech_career.get_combined_data()
    return {"data": combined_data}

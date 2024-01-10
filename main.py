from fastapi import FastAPI

from src.Patika import PatikaDevData
from src.TechCareer import TechCareerData

app = FastAPI()


@app.get("/")
async def root():
    return {"example": "Hello Worldsdsds","data":999}

#techcareerde isim,imgurl,tarih,link olarak dönüyor
@app.get("/tech")
async def get_tech_data():
    tech_career = TechCareerData('https://www.techcareer.net/bootcamp')
    tech_career.scrape_data()
    combined_data = tech_career.get_combined_data()
    return {"data": combined_data}


@app.get("/patika")
async def get_patika_data():
    patika_data = PatikaDevData('https://www.patika.dev/programs')
    patika_data.scrape_data()
    combined_data = patika_data.get_combined_data()
    print(combined_data)
    return {"data": combined_data}

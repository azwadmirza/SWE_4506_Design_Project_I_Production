from fastapi import FastAPI, HTTPException
from dataprep.eda import create_report
import pandas as pd
from decouple import config
import cloudinary
from cloudinary.uploader import upload
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
import tempfile
import os

app = FastAPI()
cloudinary.config(
    cloud_name=config('CLOUDINARY_CLOUD_NAME'),
    api_key=config('CLOUDINARY_API_KEY'),
    api_secret=config('CLOUDINARY_API_SECRET')
)
from pydantic import BaseModel

origins = [
    "*",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
  url: str
  delimiter: str

@app.post("/get_visualization")
async def fetch_url(data: RequestData):
    try:
        url = data.url
        if(url[-4:] == ".csv"):
            df = pd.read_csv(url)
        elif(url[-5:] == ".xlsx"):
            df=pd.read_excel(url)
        elif(url[-4:] == ".txt"):
            df=pd.read_csv(url, sep=data.delimiter)
        elif(url[-5:] == ".json"):
            df=pd.read_json(url)
        else:
            print("Hello World")
            raise HTTPException(status_code=400, detail="File type not supported")
        
        for column in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[column].dtype):
                df[column] = df[column].apply(lambda x: x.timestamp())
        report = create_report(df)
        with tempfile.NamedTemporaryFile(suffix='.html', dir='./visualization', delete=False) as f:
            report.save(f.name)
            response = upload(f.name, public_id='report.html', resource_type='auto')
            cloudinary_link=response["secure_url"]
        return {"cloudinary_link": cloudinary_link}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
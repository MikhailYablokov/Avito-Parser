from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import xml.etree.ElementTree as ET
import json
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

ADS_FILE = "ads.json"

def load_ads():
    if os.path.exists(ADS_FILE):
        with open(ADS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_ads(ads):
    with open(ADS_FILE, "w", encoding="utf-8") as f:
        json.dump(ads, f, ensure_ascii=False, indent=2)

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    ads = load_ads()
    return templates.TemplateResponse("upload_form.html", {"request": request, "ads": ads})

@app.post("/upload", response_class=HTMLResponse)
async def upload_xml(request: Request, xml_file: UploadFile = File(...)):
    existing_ads = load_ads()
    existing_keys = {(ad["url"] or "", ad["title"] + ad["address"]) for ad in existing_ads}

    content = await xml_file.read()
    root = ET.fromstring(content)

    new_ads = []
    for ad_elem in root.findall("ad"):
        ad = {
            "title": ad_elem.findtext("title", "").strip(),
            "price": ad_elem.findtext("price", "").strip(),
            "address": ad_elem.findtext("address", "").strip(),
            "area": ad_elem.findtext("area", "").strip(),
            "url": ad_elem.findtext("url", "").strip(),
            "date": ad_elem.findtext("date", "").strip()
        }
        key = (ad["url"], ad["title"] + ad["address"])
        if key not in existing_keys:
            new_ads.append(ad)
            existing_keys.add(key)

    existing_ads.extend(new_ads)
    save_ads(existing_ads)

    return templates.TemplateResponse("upload_form.html", {
        "request": request,
        "ads": existing_ads,
        "status": f"Загружено {len(new_ads)} новых объявлений" if new_ads else "Дубликатов не найдено"
    })

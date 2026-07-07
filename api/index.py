from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path
from io import BytesIO
import pandas as pd

app = FastAPI()

# Get absolute path to the templates folder
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    # Read uploaded Excel file into memory
    contents = await file.read()
    excel = BytesIO(contents)

    # Load Excel
    df = pd.read_excel(excel, skiprows=2)

    # Drop unwanted columns if they exist
    columns_to_drop = ["Mobile", "Email"]
    df = df.drop(
        columns=[col for col in columns_to_drop if col in df.columns]
    )

    # Clean patient names
    if "PName" in df.columns:
        df["PName"] = (
            df["PName"]
            .astype(str)
            .str.split("/")
            .str[0]
            .str.strip()
        )

    # Save cleaned dataframe to memory
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=modified_sales_report.xlsx"
        },
    )
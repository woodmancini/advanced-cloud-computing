from fastapi import APIRouter, HTTPException

router = APIRouter()

instruments = {
    "mandolin":{
        "scale":"13.875",
        "strings":"8",
        "tuning":"GDAE"
        },
    "mandola":"16",
    "octave mandolin":"21",
    "cello":"27"
}

@router.get("/")
def get_all_instruments():
    return instruments

@router.get("/{instrument_name}")
def get_instrument(instrument_name: str):
    instrument = instruments.get(instrument_name)

    if instrument is None:
        raise HTTPException(status_code=404, detail="Instrument not found")

    return instrument

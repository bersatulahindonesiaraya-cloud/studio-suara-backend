import os
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()

# Mengambil token dari Environment Variable Render
EXPECTED_TOKEN = os.getenv("API_TOKEN", "RAHASIA-ZEA-2026-AMAN")


@app.post("/clone-voice/")
async def clone_voice(
    audio: UploadFile = File(...),
    text: str = Form(...),
    token: str = Form(...),
):
  # Validasi Token Keamanan
  if token != EXPECTED_TOKEN:
    raise HTTPException(status_code=403, detail="Token keamanan tidak valid.")

  try:
    # Simpan file audio yang diunggah dari Hostinger sementara
    temp_audio_path = f"temp_{audio.filename}"
    with open(temp_audio_path, "wb") as buffer:
      buffer.write(await audio.read())

    # --- PROSES AI / KLONING SUARA ANDA DI SINI ---
    # (Untuk sementara, file audio yang masuk akan dikembalikan dulu sebagai uji coba koneksi)
    output_audio_path = temp_audio_path

    return FileResponse(
        output_audio_path,
        media_type="audio/mpeg",
        filename="hasil_kloning.mp3",
    )

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
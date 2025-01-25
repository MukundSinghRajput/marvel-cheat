import os
from pyrogram import Client, filters
from pyrogram.types import Message
from Mukund import Mukund

storage = Mukund("MukundX")
db = storage.database("marvel")

app = Client(
    "pro",
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("API_HASH"),
    session_string=os.getenv("SESSION")
)

@app.on_message(filters.photo & filters.user([7828242164]))
async def hacke(c: Client, m: Message):
    try:
        if m.caption and "/hunt" in m.caption:
            file_data = db.get(f"{m.photo.file_unique_id}")
            await m.reply(f"/hunt {file_data['name']}")
            return
        return
    except Exception:
        pass

app.run()
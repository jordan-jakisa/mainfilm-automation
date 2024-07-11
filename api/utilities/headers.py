import  os
from dotenv import load_dotenv

load_dotenv()

header = {
    "content-type": "application/json",
    "Authorization": f"Token token={os.getenv('MOCO_API_KEY')}"
}

domain = "https://kyambogo.mocoapp.com/"
import requests

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"

def download_file(filepath: str, url: str) -> None:
   response = requests.get(url, params={"User-Agent": DEFAULT_USER_AGENT})
   with open(filepath, mode="wb") as file:
        file.write(response.content)

def get_filetype(filename: str) -> str:
    return ":".join(filename.split(".")[-1].split(":")[:-1])
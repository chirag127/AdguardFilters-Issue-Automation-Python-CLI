
import os
import requests

def get_image_path(path: str, url: str) -> str:
    """
    Downloads an image from a URL if it doesn't exist locally.
    Returns the local path to the image.
    """
    if not os.path.exists(path):
        print(f"Image not found at {path}, downloading from {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(path, "wb") as f:
                f.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image: {e}")
            return ""
    else:
        print(f"Image found at {path}")
    return path

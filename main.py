import time

import numpy as np
import pyperclip

from typing import cast
from PIL import Image, ImageGrab
from paddleocr import PaddleOCR
from rich.console import Console

# Poll image from clipboard 10 times a second
POLL_INTERVAL = 1 / 10


def poll_image_from_clipboard() -> Image.Image | None:
    try:
        img = ImageGrab.grabclipboard()
        return cast(Image.Image, img)
    except OSError:
        return None


def are_images_identical(img1: Image.Image | None, img2: Image.Image | None) -> bool:
    if img1 is None or img2 is None:
        return img1 == img2

    arr1 = np.array(img1)
    arr2 = np.array(img2)

    return arr1.shape == arr2.shape and (arr1 == arr2).all()


def get_text(ocr_results) -> str:
    return "\n".join(" ".join(res.json["res"]["rec_texts"]) for res in ocr_results)


def main():
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )
    console = Console()

    prev_img = None

    console.print("Polling images from clipboard", style="bold cyan")
    while True:
        img = poll_image_from_clipboard()
        if img is None or img == prev_img:
            time.sleep(POLL_INTERVAL)
            continue

        console.print("[*] Got new image from clipboard", style="bold cyan")
        prev_img = img

        result = ocr.predict(np.array(img))
        text = get_text(result)
        console.print(f"Recognized text (written to clipboard): {text}", style="green")
        pyperclip.copy(text)


if __name__ == "__main__":
    main()

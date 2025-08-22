# miru

Simple Python OCR clipboard watcher. This is essentially the same thing as [manga-ocr](https://github.com/kha-white/manga-ocr)
but uses [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) instead for the OCR model.

`manga-ocr` is great at what it was intended for (manga), however it performs quite poorly on other fonts such as the ones
used in Japanese youtube videos, so I wrote this to make my [sentence mining](https://refold.la/roadmap/stage-2/a/basic-sentence-mining/) workflow
a bit smoother.

## Running

Ensure that you have [uv](https://github.com/astral-sh/uv) installed, then simply:

```bash
uv run main.py
```

Once the watcher is running, screenshots in your clipboard will automatically be replaced with text recognized
by the OCR, which can then be pasted into tools like [Yomitan](https://yomitan.wiki/) for looking up words.

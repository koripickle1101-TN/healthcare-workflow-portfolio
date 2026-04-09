import csv
import os
from PIL import Image, ImageDraw, ImageFont

# Create output folders
os.makedirs("exports", exist_ok=True)

WIDTH, HEIGHT = 1080, 1080

def create_slide(text, filename, bg_color, text_color):
    img = Image.new("RGB", (WIDTH, HEIGHT), color=bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 110)
    except:
        font = ImageFont.load_default()

    lines = []
    words = text.split()
    line = ""

    for word in words:
        if len(line + word) < 40:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    y_text = 150

    for line in lines:
        draw.text((100, y_text), line.strip(), fill=text_color, font=font)
        y_text += 120

    img.save(filename)


def generate_post(row, index):
    folder = f"exports/post_{index}"
    os.makedirs(folder, exist_ok=True)

    slides = [
        row["HOOK"],
        row["WORKFLOW"],
        row["BREAKDOWN"],
        row["ROOT_CAUSE"],
        row["IMPACT"],
        row["FIX"],
        row["INSIGHT"],
    ]

    for i, text in enumerate(slides):
        create_slide(
            text,
            f"{folder}/slide_{i+1}.png",
            bg_color=(15, 31, 61),
            text_color=(255, 255, 255),
        )


with open("content/workflow_content.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader, start=1):
        generate_post(row, i)

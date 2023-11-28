from PIL import Image, ImageDraw, ImageFont
def add_text(image_path, texts, coordinates_list, font_size=20, text_color=(255, 255, 255), background_color=(255, 255, 255), padding=2):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font = ImageFont.truetype(font_path, font_size)
    for text, coordinates in zip(texts, coordinates_list):
        text_bbox = draw.textbbox(coordinates, text, font=font)
        background_rect = (
            text_bbox[0] - padding,
            text_bbox[1] - padding,
            text_bbox[2] + padding,
            text_bbox[3] + padding
        )
        draw.rectangle(background_rect, fill=background_color)
        draw.text((coordinates[0] - padding, coordinates[1] - padding), text, font=font, fill=text_color)
    image.save('modified_image.jpg')
image_path = 'photo.jpeg'
texts = [
    'String text 1',
    'String text 2',
    'String text 3',
    'String text 4',
    'String text 5',
    'String text 6'
]
coordinates_list = [
    (100, 200),
    (100, 300),
    (100, 400),
    (100, 500),
    (100, 600),
    (100, 700)
]
font_size = 36
text_color = (51, 51, 51)
background_color = (255, 255, 255)
padding = 5
add_text(image_path, texts, coordinates_list, font_size, text_color, background_color, padding)

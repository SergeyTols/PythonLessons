from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (600, 400), (0, 0, 255))
draw = ImageDraw.Draw(image)

draw.circle((600, 0), radius=150, fill='yellow')

draw.text((100, 180), text="Это солнечный день", fill='yellow',
          font=ImageFont.truetype("Gabriola.ttf", 60))
draw.text((500, 380), text="Made by Sarge", fill='white',
          font=ImageFont.truetype(font=r'\PycharmProjects\PythonLessons\Fonts\Robloxian-UltraBold.ttf'),
          font_size=20)
image.save('images/deep_blue.jpg')

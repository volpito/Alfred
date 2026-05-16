import time
from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd2in13_V4

class ScreenTest:
  # 1. Setup
  epd = epd2in13_V4.EPD()
  epd.init()
  epd.Clear()
  # 2. Create Image (using e-paper dimensions)
  image = Image.new('1', (epd.width, epd.height), 255) #255 = white background
  draw = ImageDraw.Draw(image)
  font = ImageFont.load_default()
  # 3. Draw directly
  draw.text((10, 10), 'Hello Boss', font=font, fill=0)
  # 4. Push to screen
  epd.display(epd.getbuffer(image))
  # 5. Cleanup
  time.sleep(2)
  epd.sleep()

if __name__ == '__main__':
    ScreenTest().Run()

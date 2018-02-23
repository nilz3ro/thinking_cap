import board
import neopixel
import time

def glow_purple(px, t, max):
  for value in range(max):
    px[0] = (value, 0, value)
    px.show()
    time.sleep(t)

def dim_purple(px, t, max):
  nums = range(max)
  for num in nums:
    value = max - num
    px[0] = (value, 0, value)
    px.show()
    time.sleep(t)

def glow_blue(px, t, max):
  mums = range(max)
  for num in nums:
    px[0] = (value/2, 0, value)
    px.show()
    time.sleep(t)

def dim_blue(px, t, max):
  nums = range(max)
  for num in nums:
    value = max - num
    px[0] = (value/2, 0, value)
    px.show()
    time.sleep(t)

def main():
  # board.D2 is the output pin that is sewn into the hat.
  # 1 represents the number of connected pixels
  pixels = neopixel.NeoPixel(board.D2, 1)
  frame_duration = 1/60
  max_brightness = 70

  while True:
    glow_purple(pixels, frame_duration, max_brightness)
    dim_purple(pixels, frame_duration, max_brightness)
    # glow_blue(pixels, frame_duration, max_brightness)
    # dim_blue(pixels, frame_duration, max_brightness)

main()
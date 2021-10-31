import time
from plyer import notification

if __name__ == "__main__":
   while True:
      notification.notify(
      title = "It's break time",
      message = "You have been doing great. How about take small 5 min break and go for a short walk, drink water, stretch for a little bit or meditate for 5 mins. This will be great way to recharge yourself",
      app_icon =  ".\icon.ico",
      timeout = 10,
      ticker="Blue-breathe"
      )
   time.sleep(4200);

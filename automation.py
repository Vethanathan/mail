!pip install smtplib
!pip install schedule
import smtplib
import schedule
import time
from datetime import date
from datetime import datetime



holidays= ["05/10/2021","10/10/2021"]

def mail():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  current_time = current_time.split(":")
  today = date.today()
  print(current_time)
  d1 = today.strftime("%d/%m/%Y")
  if d1 in holidays and current_time[:2]==["15","01"] and current_time[-1]>"30":
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("vethabot@gmail.com", "yourpassword")
    message = "Tommorow is a holiday"
    s.sendmail("vethabot@gmail.com", "vethanathanvk@gmail.com", message)
    print("mail sent successfully")
    s.quit()
    #exit()




schedule.every(10).seconds.do(mail)
#schedule.every().day.at("20:21").do(mail)


while 1:
	schedule.run_pending()
	time.sleep(1)

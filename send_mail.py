import xlrd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
import smtplib

def im(Roll_no,Name,Event_type,Event_name,Time,Receiver):
    img = Image.open("Certificate of organiser.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("a.TTF", 45)
    font2 = ImageFont.truetype("a.TTF", 25)
    font1 = ImageFont.truetype("a.TTF", 35)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((510,320),Name,(0,0, 255),font=font)
    draw.text((485,365),Roll_no,(0,0, 255),font=font1)
    draw.text((685, 430),Event_name, (0,0, 255), font=font2)
    draw.text((490, 450),Event_type, (0,0, 255), font=font2)

    draw.text((640, 455), Time, (0,0, 255), font=font2)
    img.save('sample-out.png')
    username = 'pmanagement197'
    password = 'pr0ject1'
    sender = username + '@gmail.com'

    msg = MIMEMultipart()
    msg['Subject'] = 'Certificate of Appreciation.'
    msg['From'] = username + '@gmail.com'
    msg['Reply-to'] = username + '@gmail.com'
    msg['To'] = Receiver

    # That is what u see if dont have an email reader:
    msg.preamble = 'Multipart massage.\n'

    # Body
    part = MIMEText("Hello,\n\nPlease find attached your certificate.\n\nGreetings.")
    msg.attach(part)

    # Attachment
    part = MIMEApplication(open("sample-out.png", "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=os.path.basename("sample-out.png"))
    msg.attach(part)

    # Login
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender, password)

    # Send the email
    server.sendmail(msg['From'], msg['To'], msg.as_string())


if __name__=="__main__":
    Book = xlrd.open_workbook('participants1.xlsx')
    WorkSheet = Book.sheet_by_name('Worksheet')

    num_row = WorkSheet.nrows - 1
    row = 0

    while row < num_row:
        row += 1

        Roll_no = WorkSheet.cell_value(row, 10)
        Name = WorkSheet.cell_value(row, 2)
        Event_name = WorkSheet.cell_value(row, 8)
        Event_type = WorkSheet.cell_value(row, 7)
        Receiver= WorkSheet.cell_value(row, 3)
        Time = "Oct,2019"
        im(str(int(Roll_no)),Name,Event_type,Event_name,Time,Receiver)

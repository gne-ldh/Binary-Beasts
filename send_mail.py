# Link to Registration Form
#https://docs.google.com/forms/d/e/1FAIpQLSdFIQRmf9cm_3N8Z4ZhkyF36gcsAMOF2qcDqfy89K2kwC5YmA/viewform?usp=sf_link


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
import smtplib
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def im(Roll_no,Name,Event_type,Event_name,Time,Receiver):
    img = Image.open("Certificate of organiser.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("a.TTF", 45)
    font2 = ImageFont.truetype("a.TTF", 25)
    font1 = ImageFont.truetype("a.TTF", 35)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((510, 320), Name, (0, 0, 255), font=font)
    draw.text((485, 365), Roll_no, (0, 0, 255), font=font1)
    draw.text((685, 430), Event_name, (0, 0, 255), font=font2)
    draw.text((483, 455), Event_type, (0, 0, 255), font=font2)
    draw.text((640, 455), Time, (0, 0, 255), font=font2)


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

    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("Participants_data").sheet1
    data = sheet.get_all_records()

    data_len = len(data)
    i = 0

    while i <= data_len - 1:
        Name = data[i]['Full Name']
        Receiver = data[i]['Email Address']
        Event_type = data[i]['Event Type ']
        Event_name = data[i]['Event Name']
        Roll_no = data[i]['University Roll Number']
        Time = "Oct,2019"
        im(str(int(Roll_no)), Name, Event_type, Event_name, Time, Receiver)
        i = i+1

    print('Certificates Sent Successfully!!')




    '''Book = xlrd.open_workbook('participants1.xlsx')
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
     '''

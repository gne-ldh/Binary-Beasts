# Binary-Beasts

##Installation steps for E-Certificate generator:

1. For testing purpose open this link to Registartion Form:

https://docs.google.com/forms/d/e/1FAIpQLSdFIQRmf9cm_3N8Z4ZhkyF36gcsAMOF2qcDqfy89K2kwC5YmA/viewform?usp=sf_link

2. Simply copy Send_mail.py file in your Python environment.

3. Click the run button and it will automatically send certificates to the emails of registered users



Introduction to the Electronic Certificate
                
An Electronic Certificate is a set of data enabling identification of the holder of the Certificate, secure exchange of information with other persons and institutions and automatically sent that certificate to destined location using mail server and to verify the date & time of certification generation.


Steps involved in creating the certificate

1.	Certificate Creation
We have made a certificate template by using PIL Library i.e. Python Imaging Library used in image processing.

2.	Database Connectivity

We have made a GUI which takes data manually from a user’s site and it gets stored into an excel sheet. Data for certificate is extracted from the excel sheet described above. Django can also be used for data extraction.

3.	Data Filling

Mainly at this step information is being written through PHP form and stored in database.
Thereafter, the data is being fetched from database itself and excel sheet. And if it get matched from existing database entries & check accordingly hat who are the participants and who are the winners in any fest and their entries are done into certificate and on the final submission by administrator E-Certificate is sent at perfect recipient according to their roles.

4.	Certificate Delivery
Many times, delivery of certificates is delayed or certificates are misplaced. By this system, the generated certificate is delivered to the intended receiver via email address. This minimizes the efforts and headache of manually managing the system of certificate delivery. This is a plus point of this project.


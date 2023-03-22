import sys
import smtplib
import traceback
from datetime import datetime
from io import StringIO

from .smtp_config import SENDER, RECEIVER, MAIL_SERVER, PORT, USERNAME, PASSWORD


LOG_FILE = 'log.txt'


def log(old_function):
    def new_function(*args, **kwargs):
        with open(LOG_FILE, 'at', encoding='UTF-8') as filehandle:
            sys.stdout = filehandle
            sys.stderr = filehandle

            name = old_function.__name__
            dttm = datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y")
            arguments = ', '.join([str(arg) for arg in args]) if args else '<no pos. args>'
            kwarguments = (', '.join([f'{key}: {value}' for key, value in kwargs.items()])
                       if kwargs else '<no key-word args>')
            params = f'\t{arguments}\n\t{kwarguments}'

            print(f'"{name}" function called at {dttm}\n'
                  f'with the following params:'
                  f'\n{params}\n')
            try:
                result = old_function(*args, **kwargs)
                print(f'{name} function returned:\n{str(result)}\n\n')

            except Exception as e:
                print(f'Exception raised durning {name} function execution:\n')
                traceback.print_exc(file=filehandle)
                print('\n')
                raise e

        return result
    return new_function


def email_log(old_function):
    def new_function(*args, **kwargs):
        buffer = StringIO()
        sys.stdout = buffer
        sys.stderr = buffer
        
        def send_log(exc):
            message = buffer.getvalue()
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            
            sender_email = SENDER
            receiver_email = RECEIVER
            smtp_server = MAIL_SERVER
            smtp_port = PORT
            smtp_username = USERNAME
            smtp_password = PASSWORD

            try:
                smtp_server = smtplib.SMTP(smtp_server, smtp_port)
                smtp_server.starttls()
                smtp_server.login(smtp_username, smtp_password)
                message = message.encode('utf-8')
                smtp_server.sendmail(sender_email, receiver_email, message)
                smtp_server.quit()
                print('Email log successfully sent.')

            except smtplib.SMTPConnectError as e:
                print(f"Failed to connect to the SMTP server: {e}")
            except smtplib.SMTPAuthenticationError as e:
                print(f"Failed to authenticate with the SMTP server: {e}")
            except (smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused) as e:
                print(f"Failed to send email: {e}")
            except smtplib.SMTPDataError as e:
                print(f"Failed to send email data: {e}")
            except Exception as e:
                print(f"Unknown error occurred: {e}")
                
            if exc:
                raise exc

        name = old_function.__name__
        dttm = datetime.strftime(datetime.now(), "%H:%M:%S %d.%m.%Y")
        arguments = ', '.join([str(arg) for arg in args]) if args else '<no pos. args>'
        kwarguments = (', '.join([f'{key}: {value}' for key, value in kwargs.items()])
                       if kwargs else '<no key-word args>')
        params = f'\t{arguments}\n\t{kwarguments}'

        print(f'"{name}" function called at {dttm}\n'
              f'with the following params:'
              f'\n{params}')
        
        result = 'Exception raised during "{name}" execution!'
        error = None
        try:
            result = old_function(*args, **kwargs)
            print(f'"{name}" function returned:\n{str(result)}\n\n')

        except Exception as e:
            traceback.print_exc(file=buffer)
            error = e
            
        send_log(error)
        return(result)
            
    return new_function

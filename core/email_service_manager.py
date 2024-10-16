# core/email_service_manager.py
from core.services.gmail_service import GmailService
from core.services.outlook_service import OutlookService
from core.services.sendgrid_service import SendGridService
from core.services.smtp_service import SMTPService

from core.utils import constants

class EmailServiceManager:
    def __init__(self, service_type, user_credentials):
        self.service = self._initialize_service(service_type, user_credentials)

    def _initialize_service(self, service_type, user_credentials):
        if service_type == constants.CONST_GMAIL:
            return GmailService(user_credentials)
        elif service_type == constants.CONST_OUTLOOK:
            return OutlookService(user_credentials)
        elif service_type == constants.CONST_SENDGRID:
            return SendGridService(user_credentials)
        elif service_type == constants.CONST_SMTP:
            return SMTPService(user_credentials)
        else:
            raise ValueError("Unsupported email service type")

    def send_email(self, *args, **kwargs):
        return self.service.send_email(*args, **kwargs)

    def monitor_emails(self, *args, **kwargs):
        return self.service.monitor_emails(*args, **kwargs)

    def delete_email(self, *args, **kwargs):
        return self.service.delete_email(*args, **kwargs)

    def move_email(self, *args, **kwargs):
        return self.service.move_email(*args, **kwargs)

    def forward_email(self, *args, **kwargs):
        return self.service.forward_email(*args, **kwargs)

    def reply_email(self, *args, **kwargs):
        return self.service.reply_email(*args, **kwargs)

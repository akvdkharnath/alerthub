# core/services/smtp_service.py
from core.base_email_service import BaseEmailService


class SMTPService(BaseEmailService):
    def __init__(self, user_credentials):
        super().__init__(user_credentials)

import ssl
import smtplib
from email.mime.text import MIMEText

from backend.config import get_settings


def verify_email(receiver_email: str, key: str) -> None:
    settings = get_settings()
    # Пока костыль, как написать без хардкода хз, мб вынести в отдельный файлик и оттуда подтягивать
    url = f"{settings.APP_HOST}:{settings.APP_PORT}{settings.PATH_PREFIX}/user/verify/{key}"
    msg = MIMEText(f"Для подтверждения адреса электронной почты введите в приложении данный код:\n{key}\n\n"
                   f"Не получается ввести код? Вставьте следующую ссылку в ваш браузер:\n{url}")
    msg["Subject"] = "Код для подтверждения электронной почты"
    context = ssl.create_default_context()
    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_EMAIL, receiver_email, msg.as_string())

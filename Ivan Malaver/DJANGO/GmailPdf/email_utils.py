from django.core.mail import send_mail
from django.conf import settings

def send_email_notification(user, subject, message):
    """
    Envía una notificación por correo electrónico.

    Args:
        user: Usuario destinatario.
        subject: Asunto del email.
        message: Contenido del mensaje.
    
    Returns:
        bool: True si el correo se envió correctamente, False si hubo error.
    """
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False
        )
        return True

    except Exception as e:
        print(f"Error enviando email: {str(e)}")
        return False

import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

# 1) Genera la gráfica en PDF
def generar_grafica_pdf():
    buffer = BytesIO()

    # Crear gráfica
    plt.plot([1, 2, 3, 4], [10, 20, 15, 30])
    plt.title("Mi primera gráfica en PDF")

    # Guardarla como PDF en memoria
    plt.savefig(buffer, format="pdf")
    plt.close()

    buffer.seek(0)
    return buffer

    


# 2) Vista que envía el PDF por email
def enviar_pdf(request):

    pdf_buffer = generar_grafica_pdf()

    email = EmailMessage(
        subject="Tu gráfica PDF",
        body="Aquí tienes tu archivo PDF.",
        from_email=settings.EMAIL_HOST_USER,
        to=["sebasbel11tran@gmail.com"]   # ← AQUI CAMBIAS EL DESTINATARIO
    )

    email.attach(
        "grafica.pdf",
        pdf_buffer.getvalue(),
        "application/pdf"
    )

    email.send()

    return HttpResponse("Correo enviado correctamente.")

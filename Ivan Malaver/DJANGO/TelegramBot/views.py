from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import json
import asyncio
import threading


# ============================
# CONFIG BOT
# ============================

TOKEN = settings.TELEGRAM_BOT_TOKEN
application = Application.builder().token(TOKEN).build()


# ============================
# HANDLERS
# ============================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot en Django. 😊")


application.add_handler(CommandHandler("start", start))

async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! ¿Cómo estás?")
    
application.add_handler(CommandHandler("hola", hola))


async def hacer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Este es mi primer bot❤️")
application.add_handler(CommandHandler("hacer", hacer))

# ============================
# LOOP 
# ============================

loop = asyncio.new_event_loop()

def loop_thread():
    asyncio.set_event_loop(loop)
    loop.run_forever()   # 🔥 El loop SIEMPRE estará corriendo

threading.Thread(target=loop_thread, daemon=True).start()

# Inicializar el bot dentro del loop
asyncio.run_coroutine_threadsafe(application.initialize(), loop)


# ============================
# WEBHOOK VIEW
# ============================

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            update = Update.de_json(data, application.bot)

            # Procesar el update dentro del loop REAL que está corriendo
            asyncio.run_coroutine_threadsafe(
                application.process_update(update),
                loop
            )

            return JsonResponse({"ok": True})

        except Exception as e:
            print("ERROR WEBHOOK:", e)
            return JsonResponse({"ok": False})

    return JsonResponse({"ok": False})

#https://api.telegram.org/bot7933146444:AAEyCSIc5-j30Y0Uf5yGurkTc-pfIQDBtAI/setWebhook?url=https://averagely-gemeled-lekisha.ngrok-free.dev/webhook/
#Esta es la url


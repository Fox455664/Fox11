import nest_asyncio
nest_asyncio.apply()  # يتم استدعاؤه مرة واحدة فقط في بداية البرنامج

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQueryResultArticle, InputTextMessageContent

app = Client("7107627916:AAExR51c8AKgmxvtpgj00kb2O9S3FwhaAqc")

@app.on_inline_query()
async def answer(client, inline_query):
    user_id = inline_query.from_user.id  # استخدام مُعرف المستخدم بدلاً من اسم المستخدم
    title = f"هذه همسة سرية لك"
    message_text = f"هذه همسة سرية لك"
    results = [
        InlineQueryResultArticle(
            title=title,
            input_message_content=InputTextMessageContent(message_text),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("اضغط للرؤية", callback_data=f"{user_id}or{message_text}")
            ]])
        )
    ]
    await client.answer_inline_query(inline_query.id, results)

@app.on_callback_query()
async def callback_query_answer(client, callback_query: CallbackQuery):
    data = callback_query.data
    if data and callback_query.from_user:
        ex = data.split("or")
        if str(callback_query.from_user.id) in ex:
            await callback_query.answer(ex[1], show_alert=True)
        else:
            await callback_query.answer("الرسالة ليست لك", show_alert=True)

@app.on_message(filters.command("همسه"))
async def start(client, message: Message):
    await message.reply(
        "مرحبًا\n"
        "🌐 أنا بوت أهمسلي.\n\n"
        "💬 يمكنك استخدامي لإرسال رسائل سرية (همسات) في أي مجموعة تشاء.\n"
        "🔮 أعمل عن بُعد، هذا يعني أنك تستطيع استخدامي دون الحاجة لوجودي في المجموعة.\n"
        "💌 طريقة استخدامي سهلة جدًا، قم بتحويل أي رسالة من الشخص الذي تريد أن تهمس له هنا\n\n"
        "هناك طرق أخرى للاستخدام يمكنك رؤيتها عبر الضغط على 'طرق أخرى لاستخدام البوت'",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("المطور", url="t.me/F_o_x_5")
        ]])
    )

# دالة main التي تُستدعى لتشغيل البوت
async def main():
    async with app:
        await app.start()
        # ... كود البوت
        await app.stop()

# تشغيل حلقة الحدث
if __name__ == "__main__":
    asyncio.run(main())

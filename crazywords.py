from hoshino import Service
from nonebot.message import CQEvent
from .generate import generate_txt

sv = Service('crazywords')


@sv.on_prefix(('发疯'))
async def send_crazywords(bot, event: CQEvent):
    name = event.message.extract_plain_text().strip()
    if not name:
        await bot.finish(event, '请发送[发疯 对象]', at_sender=True)
    result = generate_txt(name)
    await bot.send(event, result, at_sender=True)

import asyncio

from aiogram import Bot, Dispatcher

from app.config_loader import load_config, Config
from app.database import build_engine, build_session_factory
from app.telegram.middlewares import DBSessionMiddleware, AuthMiddleware
from app.telegram.handlers import include_routers
from app.s3 import S3Service


async def main() -> None:
    config = load_config(Config)

    engine = await build_engine(config.database)
    session_factory = build_session_factory(engine)

    s3 = S3Service(config.s3)

    bot = Bot(token=config.bot.token)
    dp = Dispatcher(bot=bot, s3=s3)

    dp.update.outer_middleware(DBSessionMiddleware(session_factory))
    dp.update.middleware(AuthMiddleware())

    include_routers(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

from aiogram import Bot, Dispatcher

from app.config_loader import load_config, Config
from app.database import build_engine, build_session_factory
from app.telegram.middlewares import DBSessionMiddleware, AuthMiddleware
from app.s3 import S3Service


async def main() -> None:
    config = load_config(Config)

    s3 = S3Service(config=config.s3)

    engine = await build_engine(config.database)
    session_factory = build_session_factory(engine)

    bot = Bot(token=config.bot.token)
    dp = Dispatcher(bot=bot, s3=s3)

    dp.update.outer_middleware(DBSessionMiddleware(session_factory))
    dp.update.outer_middleware(AuthMiddleware())

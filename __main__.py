from aiogram import Bot, Dispatcher

from app.config_loader import load_config, Config
from app.database import build_engine, build_session_factory
from app.telegram.middlewares import DBSessionMiddleware, AuthMiddleware


async def main() -> None:
    config = load_config(Config)
    bot = Bot(token=config.bot.token)
    dp = Dispatcher(bot=bot)

    engine = await build_engine(config.database)
    session_factory = build_session_factory(engine)
    dp.update.outer_middleware(DBSessionMiddleware(session_factory))

from dataclasses import dataclass


@dataclass(frozen=True)
class BotConfig:
    token: str


@dataclass(frozen=True)
class WebhookConfig:
    domain: str
    webhook_url: str
    port: int

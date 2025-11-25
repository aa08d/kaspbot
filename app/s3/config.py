from dataclasses import dataclass


@dataclass(frozen=True)
class S3Config:
    access_key: str
    secret_key: str
    bucket_name: str
    region_name: str

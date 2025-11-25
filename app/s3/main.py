from typing import BinaryIO

import aioboto3

from .config import S3Config


class S3Service:
    def __init__(self, config: S3Config) -> None:
        self.config = config
        self.session = aioboto3.Session(
            aws_access_key_id=self.config.access_key,
            aws_secret_access_key=self.config.secret_key,
            region_name=self.config.region_name,
        )

    async def upload_file(self, file: BinaryIO, file_name: str) -> None:
        async with self.session.client("s3") as s3:
            await s3.put_object(Bucket=self.config.bucket_name, Key=file_name, Body=file)

    async def download_file(self, file_name: str) -> bytes:
        async with self.session.client("s3") as s3:
            response = await s3.get_object(Bucket=self.config.bucket_name, Key=file_name)
            file = await response["Body"].read()
            return file

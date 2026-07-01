from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.configs import settings, logger


class MongoDBConnection:
    client: AsyncIOMotorClient = None
    database: AsyncIOMotorDatabase = None

    @classmethod
    async def dbConnect(cls) -> None:
        try:
            logger.info("Connecting to MongoDB...")

            cls.client = AsyncIOMotorClient(
                settings.mongo_uri,
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=10000,
                socketTimeoutMS=10000,
                maxPoolSize=50,
                minPoolSize=5,
            )

            await cls.client.server_info()
            cls.database = cls.client[settings.MONGO_DBNAME]

            logger.info("MongoDB connection established successfully.")

        except Exception as error:
            logger.error(f"MongoDB connection failed: {error}")

            if cls.client:
                cls.client.close()
                cls.client = None
                cls.database = None
            raise
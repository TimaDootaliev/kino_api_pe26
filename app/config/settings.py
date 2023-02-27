from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_ENGINE: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    @property
    def db_url(self):
        return '{engine}://{user}:{password}@{host}:{port}/{db_name}'.format(
            engine=self.DB_ENGINE,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            db_name=self.DB_NAME
        )
    
    class Config:
        env_file = '.env'


settings = Settings()

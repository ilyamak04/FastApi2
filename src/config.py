from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    echo: bool = True


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 30


class Settings(BaseSettings):
    db: DbSettings = DbSettings()

    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()
raw_url = os.environ.get("DATABASE_URL")
if not raw_url:
    raise RuntimeError("DATABASE_URL missing")

# ⇢ URL-encode the password in case it contains ! or @
p = urllib.parse.urlparse(raw_url)
safe_pw = urllib.parse.quote_plus(p.password or "")
SQLALCHEMY_URL = f"postgresql://{p.username}:{safe_pw}@{p.hostname}:{p.port}{p.path}"

engine = create_engine(
    SQLALCHEMY_URL,
    connect_args={"sslmode": "require"},  # Supabase needs SSL
    pool_pre_ping=True,                   # drops dead connections cleanly
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

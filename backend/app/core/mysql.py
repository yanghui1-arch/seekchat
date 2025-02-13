from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/seekchat'
# 创建同步引擎
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# 同步会话类
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False
)

# 所有models都需要继承这个类, Session用来和数据库交互的
Base = declarative_base()

# 同步获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

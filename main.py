from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configure CORS
origins = ["http://localhost", "http://localhost:3000"]  # Add your frontend URL(s) here

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Models
Base = declarative_base()


class ArticleDB(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    article_no = Column(Integer, index=True)
    currency = Column(String, index=True)
    provider_no = Column(String, index=True)
    provider = Column(String, index=True)
    price = Column(Float)


DATABASE_URL = "mysql+mysqlconnector://root:@localhost/irecharge"  # Update with your MySQL database info
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic model for request and response
class Article(BaseModel):
    article_no: int
    currency: str
    provider_no: str
    provider: str
    price: float


# CRUD operations
@app.get("/articles/", response_model=List[Article])
async def read_articles(db: Session = Depends(get_db)):
    articles = db.query(ArticleDB).all()
    return articles


@app.get("/articles/{article_no}", response_model=Article)
async def read_article(article_no: int, db: Session = Depends(get_db)):
    article = db.query(ArticleDB).filter(ArticleDB.article_no == article_no).first()
    if article:
        return article
    raise HTTPException(status_code=404, detail="Article not found")


@app.post("/articles/", response_model=Article)
async def create_article(article: Article, db: Session = Depends(get_db)):
    db_article = ArticleDB(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return article


@app.put("/articles/{article_no}", response_model=Article)
async def update_article(article_no: int, updated_article: Article, db: Session = Depends(get_db)):
    db.query(ArticleDB).filter(ArticleDB.article_no == article_no).update(updated_article.dict())
    db.commit()
    return updated_article


@app.delete("/articles/{article_no}", response_model=Article)
async def delete_article(article_no: int, db: Session = Depends(get_db)):
    deleted_article = db.query(ArticleDB).filter(ArticleDB.article_no == article_no).first()
    if deleted_article:
        db.delete(deleted_article)
        db.commit()
        return deleted_article
    raise HTTPException(status_code=404, detail="Article not found")

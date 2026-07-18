from sqlalchemy import Column, String, Text, ForeignKey, JSON
from backend.app.models.base import BaseModel

class Category(BaseModel):
    __tablename__ = "blog_categories"
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)

class Blog(BaseModel):
    __tablename__ = "blogs"
    
    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    content = Column(Text, nullable=False)
    excerpt = Column(Text, nullable=True)
    
    # Meta & SEO
    meta_title = Column(String(255), nullable=True)
    meta_description = Column(Text, nullable=True)
    faqs = Column(JSON, nullable=True) # Storing auto-generated FAQs
    
    category_id = Column(ForeignKey("blog_categories.id"))
    author_id = Column(ForeignKey("users.id"))
  

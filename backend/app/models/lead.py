from sqlalchemy import Column, String, Integer, ForeignKey
from backend.app.models.base import BaseModel

class Lead(BaseModel):
    __tablename__ = "leads"
    
    name = Column(String(100), nullable=True)
    email = Column(String(255), index=True, nullable=True)
    whatsapp_number = Column(String(20), index=True, nullable=True)
    
    source = Column(String(50), nullable=False) # e.g., 'whatsapp_widget', 'paper_trade_signup'
    utm_campaign = Column(String(100), nullable=True)
    
    # Lead Scoring Engine Field
    lead_score = Column(Integer, default=0, index=True) 
    status = Column(String(50), default="new", index=True) # new, contacted, converted

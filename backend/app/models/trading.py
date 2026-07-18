from sqlalchemy import Column, String, Numeric, ForeignKey, JSON, Enum
from backend.app.models.base import BaseModel
import enum

class OrderType(str, enum.Enum):
    BUY = "BUY"
    SELL = "SELL"

class Wallet(BaseModel):
    __tablename__ = "wallets"
    user_id = Column(ForeignKey("users.id"), unique=True, nullable=False)
    balance = Column(Numeric(15, 2), default=1000000.00) # 10 Lakh starting virtual margin

class Order(BaseModel):
    __tablename__ = "orders"
    user_id = Column(ForeignKey("users.id"), nullable=False)
    instrument = Column(String(50), index=True, nullable=False) # e.g., NIFTY, BANKNIFTY
    order_type = Column(Enum(OrderType), nullable=False)
    quantity = Column(Numeric(10, 4), nullable=False)
    execution_price = Column(Numeric(15, 2), nullable=False)
    
    # AI Coaching & Garuda Integration
    # Storing why the trade was taken and market sentiment at that exact second
    ai_trade_rationale = Column(Text, nullable=True)
    market_context_snapshot = Column(JSON, nullable=True) # FII/DII data & sentiment at execution time

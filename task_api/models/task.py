from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from task_api.models.database import Base


class Task(Base):
    __tablename__ = 'Task'

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    title = Column(String(255))
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('Category.category_id'))
    status = Column(String(50))
    due_date = Column(Date)

    user = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")

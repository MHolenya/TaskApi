from sqlalchemy import Column, Integer, String
from task_api.models.database import Base


# Create User model
class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)  # category id

    def __repr__(self):
        chain = f'<Categoty{self.category_id}>, name={self.name}'
        return chain

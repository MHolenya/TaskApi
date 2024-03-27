from sqlalchemy import Column, Integer, String
from task_api.models.database import Base


# Create User model
class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), primary_key=True, nullable=False,
                      unique=True)
    password = Column(String(120), primary_key=True,
                      nullable=False)
    email = Column(String(256), primary_key=True, nullable=False,
                   unique=True)

    def __repr__(self):
        chain = f'<User{self.user_id}>, username={
            self.username}, email={self.email}'
        return chain

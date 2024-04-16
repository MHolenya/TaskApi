from sqlalchemy import Column, Integer, String
from task_api.models.database import Base


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    password = Column(String(120), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(256), nullable=False, unique=True)

    def __repr__(self):
        chain = f'<User{self.user_id}>, username={
            self.username}, email={self.email}'
        return chain

    # function to chek if username already exists
    def chek_username(username: str):
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return True
        else:
            return False

    # function to chek if email already exists
    def chek_email(email: str):
        existing_email = User.query.filter_by(email=email).first()

        if existing_email:
            return True
        else:
            return False

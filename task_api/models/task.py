from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from task_api.models.database import Base


class Task(Base):
    __tablename__ = 'task'

    task_id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

    title = Column(String(255), nullable=False)
    description = Column(String(255))

    category_id = Column(Integer, ForeignKey(
        'category.category_id'), nullable=False)

    status = Column(String(50), nullable=False)
    due_date = Column(Date, nullable=False)

    user = relationship('User')
    category = relationship('Category')

    # --------------

    def to_dict(tasks):

        if type(tasks) is list:
            task_list: list = [{'task_id': task.task_id,
                                'user_id': task.user_id,
                                'category_id': task.category_id,
                                'title': task.title,
                                'description': task.description,
                                'status': task.status,
                                'due_date': task.due_date.strftime("%Y-%m-%d"),
                                }for task in tasks]
        else:
            task_list = {'task_id': tasks.task_id,
                         'user_id': tasks.user_id,
                         'category_id': tasks.category_id,
                         'title': tasks.title,
                         'description': tasks.description,
                         'status': tasks.status,
                         'due_date': tasks.due_date.strftime("%Y-%m-%d"),
                         }
        return task_list

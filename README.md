## TaskApi

### Users Blueprint (`users_bp`)

- **GET** `/user<int:user_id>`
  - Retrieves user details by user ID.
  
- **POST** `/register_user`
  - Creates a new user.
  
- **DELETE** `/user/<int:user_id>`
  - Deletes a user by user ID.
  
- **PUT** `/user/<int:user_id>`
  - Updates user details by user ID.

### Tasks Blueprint (`tasks_bp`)

- **GET** `/tasks`
  - Retrieves details of all tasks.
  
- **GET** `/task/<int:task_id>`
  - Retrieves details of a specific task by task ID.
  
- **POST** `/task`
  - Creates a new task.
  
- **DELETE** `/task/<int:task_id>`
  - Deletes a task by task ID.
  
- **PUT** `/task/<int:task_id>`
  - Updates task details by task ID.

### Categories Blueprint (`category_bp`)

- **GET** `/categories`
  - Retrieves details of all categories.
  
- **GET** `/category/name/<name>`
  - Retrieves details of a specific category by name.
  
- **GET** `/category/<int:category_id>`
  - Retrieves details of a specific category by category ID.
  
- **POST** `/category`
  - Creates a new category.
  
- **DELETE** `/category/<int:category_id>`
  - Deletes a category by category ID.
  
- **PUT** `/category/<int:category_id>`
  - Updates category details by category ID.

### Models

- **User**: Represents a user with attributes like user ID, username, email, and password.
- **Task**: Represents a task with attributes like task ID, user ID, title, description, category ID, status, and due date.
- **Category**: Represents a category with attributes like category ID and name.

### Database Management

- The program uses SQLAlchemy for database management.
- It creates a MySQL database engine and a scoped session for interacting with the database.
- Database initialization is performed using the `init_db` function.
- Tables for users, tasks, and categories are defined using SQLAlchemy's declarative base.

### Error Handling

- Database errors are handled using try-except blocks, and appropriate JSON responses are returned with error messages.

Aqui está a versão organizada e mais clara do seu README para o projeto **Sum and Average API**, com as instruções separadas para rodar o projeto com ou sem Docker.

---

# Sum and Average API

This API allows you to sum and calculate the average of a list of integers. It is built using the Django REST Framework (DRF) and is Dockerized for easy execution in any environment.

## API Structure

The API consists of two main endpoints:

- **Sum**
  - **POST /api/sum/**: Accepts a list of numbers and returns their sum.

- **Average**
  - **POST /api/average/**: Accepts a list of numbers and returns their average.

The API is configured to run in a Docker container and includes Swagger UI for interactive documentation.

---

## How to Run the Application on Your Machine

### 1. How to Run the Project Locally (Without Docker)

If Docker is not supported or you prefer to run the project locally, follow these steps to set up and run the API on your machine using a **virtual environment (venv)**.

#### Prerequisites:
- Python 3.8 or higher installed.
- Git (optional, only needed if cloning the repository).

#### Step-by-Step Guide:

1. **Clone the Repository** (if you haven't already):
   ```bash
   git clone https://github.com/Hansdonnersa/Restf.Py.git  
   cd Restf.Py  
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   (You will see `(venv)` in the terminal, indicating the environment is active).

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the API**:
   - **API Base URL**:
     - `http://127.0.0.1:8000/api/sum`
     - `http://127.0.0.1:8000/api/average`
   - **Interactive Documentation (DRF UI)**:
     - `http://127.0.0.1:8000/swagger/`

#### Useful Commands:
- **Deactivate the virtual environment**:
   ```bash
   deactivate
   ```

- **Restart the server** (after code changes):
   - Press `Ctrl + C` in the terminal and run again:
     ```bash
     python manage.py runserver
     ```

---
Docker Installation Notice:

Unfortunately, the Docker installation is not working correctly at the moment because the development machine is not supporting the installation properly. As a result, running the project via Docker is currently unavailable. However, the project can be run without issues using a virtual environment (venv), and instructions for this setup are provided in the "How to Run the Project Locally (Without Docker)" section.

We are working to resolve the issue and provide a solution that will allow the project to run via Docker soon. Thank you for your understanding!
### 2. How to Run the Project with Docker

If your machine supports Docker, follow these steps to run the project in a Docker container.

#### Prerequisites:
- Docker and Docker Compose installed on your machine.
- Git (optional, for cloning the repository).

#### Step-by-Step Guide:

1. **Clone the Repository** (if you haven't already):
   ```bash
   git clone https://github.com/Hansdonnersa/Restf.Py.git  
   cd Restf.Py
   ```

2. **Start the Containers**:
   - Run the following command to build the Docker image and start the container:
     ```bash
     docker-compose up --build
     ```

3. **Access the API**:
   - Once the container is running, access the API at:
     - `http://localhost:8000/api/`

4. **Test the Endpoints**:
   - Use **Swagger UI** for interactive testing:
     - `http://localhost:8000/swagger/`
   - Alternatively, use tools like **curl** or **Postman**.

5. **Stop the Containers** (when finished):
   - Press `Ctrl + C` in the terminal where `docker-compose up` is running, then execute:
     ```bash
     docker-compose down
     ```

---

## Example Requests and Responses

### **Sum**

- **Request**:
  ```json
  {
    "numbers": [1, 2, 3, 4, 5]
  }
  ```

- **Response**:
  ```json
  {
    "sum": 15
  }
  ```

### **Average**

- **Request**:
  ```json
  {
    "numbers": [10, 20, 30, 40, 50]
  }
  ```

- **Response**:
  ```json
  {
    "average": 30.0
  }
  ```

---

## Project Structure

- **Dockerfile**: Defines the Docker image for the application.
- **docker-compose.yml**: Configures services (application and database, if needed).
- **requirements.txt**: Lists project dependencies.
- **README.md**: Project documentation (this file).
- **api/**: Contains API endpoints.
- **manage.py**: Django project management script.

---

## Repository Link

Access the repository on GitHub:
- [Restf.Py GitHub Repository](https://github.com/Hansdonnersa/Restf.Py)

---


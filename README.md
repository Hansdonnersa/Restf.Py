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

Here’s the improved and well-structured version in English:

---

### 3.1. **Possible Solutions**  

If you encounter issues with the virtual environment (`venv`), follow these steps:

1. **Try updating `pip` first:**  

   Run the following commands to ensure `pip` is up to date:  

   ```bash
   python -m ensurepip --upgrade
   python -m pip install --upgrade pip
   ```

2. **If this has no effect**, follow these steps to reset the virtual environment:  

   - **Delete the `venv` folder** manually:  

     Navigate to your project directory and remove the `venv` folder.  

   - **Recreate the virtual environment:**  

     After deleting the folder, create a new virtual environment by running:  

     ```bash
3.9
     python.exe -m pip install --upgrade pip
     pip install drf-yasg
     ou 
     drf-yasg==1.24.0
     ou 
     pip install drf-yasg==1.21.9


     ```
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   if error gos to -3.9

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

## Project Structure

- **requirements.txt**: Lists project dependencies.
- **README.md**: Project documentation (this file).
- **api/**: Contains API endpoints.
- **manage.py**: Django project management script.

---

## Repository Link

Access the repository on GitHub:
- [Restf.Py GitHub Repository](https://github.com/Hansdonnersa/Restf.Py)

---


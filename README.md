# Urine strip analyzer
This project is built using Django and Django Rest Framework (DRF), with OpenCV for processing images. It analyzes uploaded urine strip images to identify and extract RGB values for 10 different colors.

## Installation
To run the Resume Reviewer locally, follow these steps:

1. Create a Virtual Environment (Optional):
   ```bash
   python -m venv venv
   
2. Activate Virtual Environment:
   - On Windows:
     ```bash
     venv\Scripts\activate

   - On Mac:
     ```bash
     source venv/bin/activate

3. Fork and clone the repository:
   ```bash
   git clone https://github.com/your-username/Urine_strip_analyzer.git

4. Navigate to the Project Directory:
   ```bash
   cd Urine_strip_analyzer

5. Install Dependencies:
   ```bash
   pip install -r requirements.txt

6. Run development server:
   ```bash
   python manage.py runserver

7. Navigate to webpage:
   ```bash
   http://localhost:8000/api/

## Installation Using Docker

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/your-username/Urine_strip_analyzer.git

2. Navigate to the Project Directory:
   ```bash
   cd Urine_strip_analyzer

3. Start Docker containers:
   ```bash
   docker-compose up --build

4. Navigate to webpage:
   ```bash
   http://localhost:8000/api/

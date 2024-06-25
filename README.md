# Urine strip analyzer
This project is built using Django and Django Rest Framework (DRF), with OpenCV for processing images. It analyzes uploaded urine strip images to identify and extract RGB values for 10 different colors.

## Installation
To run the Resume Reviewer locally, follow these steps:

1. Create a Virtual Environment (Optional):
   
   ```bash
   python -m venv venv
   
3. Activate Virtual Environment:
   
   - On Windows:
     
     ```bash
     venv\Scripts\activate

   - On Mac:
     
     ```bash
     source venv/bin/activate

4. Fork and clone the repository:
   
   ```bash
   git clone https://github.com/your-username/Urine_strip_analyzer.git

5. Navigate to the Project Directory:
   
   ```bash
   cd Urine_strip_analyzer

6. Install Dependencies:
   
   ```bash
   pip install -r requirements.txt

7. Run development server:
   
   ```bash
   python manage.py runserver

8. Navigate to webpage:
   
   ```bash
   http://localhost:8000/api/

## Installation Using Docker

1. Fork and clone the repository:
   
   ```bash
   git clone https://github.com/your-username/Urine_strip_analyzer.git

3. Navigate to the Project Directory:
   
   ```bash
   cd Urine_strip_analyzer

4. Start Docker containers:
   
   ```bash
   docker-compose up --build

5. Navigate to webpage:
   
   ```bash
   http://localhost:8000/api/

## Usage
Once the development server is running, you can access the application in your web browser at http://localhost:8000/api/ to upload a urine strip image for analysis.

![image](https://github.com/rohitsrma/Urine_strip_analyzer/assets/111359305/3c2d6d7a-960b-474c-8d63-aa0804abe956)

![image](https://github.com/rohitsrma/Urine_strip_analyzer/assets/111359305/4918d106-f82f-4d2e-98c6-162aa2b6bc1b)

## Using API Testing Tools
You can use an API testing tool to send a POST request to http://localhost:8000/api/, adding the image file in the request body as form-data.

![Screenshot (65)](https://github.com/rohitsrma/Urine_strip_analyzer/assets/111359305/68ee90ce-42b6-4f3b-b037-0ad1636ba204)

## Detection

![Screenshot (64)](https://github.com/rohitsrma/Urine_strip_analyzer/assets/111359305/4f282e84-f7bd-4d89-86aa-78fe906c2486)



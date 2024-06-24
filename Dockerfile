FROM python:3.11.4

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /analyzer_project

COPY requirements.txt /analyzer_project/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /analyzer_project/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

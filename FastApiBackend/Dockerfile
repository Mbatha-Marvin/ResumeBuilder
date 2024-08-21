FROM python:3.11.6-alpine

WORKDIR /FastApiBackend

# Copy requirements.txt to install dependencies
COPY requirements.txt requirements.txt

# Install dependencies from requirements.txt
RUN pip install --only-binary=:all: -r requirements.txt

# Copy the rest of the application code
COPY . .

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
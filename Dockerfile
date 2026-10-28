FROM python:3.11-slim
WORKDIR /app
COPY hello.py test_hello.py ./
RUN pip install --no-cache-dir pytest
CMD ["python", "hello.py"]
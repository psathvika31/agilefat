FROM python:3.10-slim
WORKDIR /app
COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt
COPY main.py .
EXPOSE 5000
CMD ["python", "main.py"]
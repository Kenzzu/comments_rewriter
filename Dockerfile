FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install "python-dotenv[cli]"
CMD ["python", "comments_rewriter.py" ]
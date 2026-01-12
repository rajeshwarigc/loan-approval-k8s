FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn scikit-learn
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8081"]

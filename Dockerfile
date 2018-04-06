FROM python:3.6

RUN pip install --no-cache-dir requests
COPY fetch.py .
ENTRYPOINT ["python", "fetch.py"]

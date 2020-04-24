FROM python:3

COPY . /app
WORKDIR /app
RUN pip install -r req.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
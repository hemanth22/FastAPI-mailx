FROM python:3.9
WORKDIR /code
COPY * /code/
RUN chmod -R 777 /code/;find / -type d -iname cachecontrol;pip install --no-cache-dir --upgrade pip;pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

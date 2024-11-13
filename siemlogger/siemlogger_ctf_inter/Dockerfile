FROM python:3.11-alpine

WORKDIR /home/user/

# copy server code
COPY server /home/user

RUN pip install -r /home/user/requirements.txt


CMD ["python", "app.py"]

FROM python:3-alpine
WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "flask", "run"]

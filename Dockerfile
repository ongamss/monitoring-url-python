FROM python:3.9-slim 

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install  --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./filter_query.py"]

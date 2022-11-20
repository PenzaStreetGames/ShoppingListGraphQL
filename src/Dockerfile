FROM python:3.10.5-alpine

WORKDIR /usr/src/app/shoping_list

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]

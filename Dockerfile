FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir feeds
RUN mkdir logs

COPY . .

RUN chmod +x ./run.sh

CMD ["bash"]
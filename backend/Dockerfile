FROM frolvlad/alpine-python3

WORKDIR /usr/src/app

COPY req.txt ./
RUN pip3 install --no-cache-dir -r req.txt

EXPOSE 5000

COPY . .

CMD [ "python3", "app.py" ]
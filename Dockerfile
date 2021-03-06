FROM python

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

# EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD ["app.py"]

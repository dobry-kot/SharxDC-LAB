FROM python:3.6
RUN useradd myapp
RUN mkdir -p /opt/myapp/
WORKDIR /opt/myapp
COPY . /opt/myapp
RUN chown -R  myapp:myapp /opt/myapp
RUN pip install --upgrade pip && pip install -r requirements.txt
USER myapp
EXPOSE 64500
ENTRYPOINT ["python3.6", "/opt/myapp/main.py"]

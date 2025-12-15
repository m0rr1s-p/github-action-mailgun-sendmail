FROM python:3.14-alpine3.22

COPY requirements.txt /action/requirements.txt
RUN pip install --upgrade --force --no-cache-dir pip && \
    pip install --upgrade --force --no-cache-dir -r /action/requirements.txt

COPY sendmail.py /action/sendmail.py

ENTRYPOINT ["python", "/action/sendmail.py"]
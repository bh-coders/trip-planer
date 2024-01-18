FROM python:3.12

WORKDIR /workspace
ADD . /workspace

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["src.main:app", "--host", "0.0.0.0","--port", "80"]
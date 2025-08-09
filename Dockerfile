FROM python:3.11-slim

WORKDIR /code

RUN apt-get update \
    && apt-get install -y build-essential libpq-dev --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only dependency files first for caching
COPY pyproject.toml uv.lock /code/

# Install dependencies
RUN pip install --upgrade pip \
    && pip install uv \
    && uv sync

COPY . /code

ENV PYTHONUNBUFFERED=1

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

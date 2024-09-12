# Use an official Python runtime as a parent image
FROM python:3.12.6

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any Python dependencies required for the bot
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (optional, if your bot needs to interact with any external service through a specific port)
EXPOSE 3000

# Environment variables (this assumes you will pass them when running the container)
ENV BOT_TOKEN=7320287650:AAE2yzMTLv7gcZ2FZtE-64pcQMSILt9rDWU
ENV API_ID=22039242
ENV API_HASH=8a9e48c643bd8934962effbc15372878

# Run the bot when the container launches
CMD ["sh", "-c", "python main.py && python test.py"]
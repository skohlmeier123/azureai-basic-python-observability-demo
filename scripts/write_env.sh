#!/bin/bash

# Define the .env file path
ENV_FILE_PATH="src/.env"

# Clear the contents of the .env file
> $ENV_FILE_PATH

echo "AZURE_AIPROJECT_CONNECTION_STRING=$(azd env get-value AZURE_AIPROJECT_CONNECTION_STRING)" >> $ENV_FILE_PATH
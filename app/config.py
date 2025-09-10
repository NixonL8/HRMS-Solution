import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # AWS Credentials (do NOT hardcode keys!)
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')  # Match what your app expects
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION', 'ap-south-1')

    # DynamoDB Tables
    USER_TABLE = 'F13_HRMS_Users'
    EMPLOYEE_TABLE = 'F13_HRMS_Employees'
    LEAVE_TABLE = 'F13_HRMS_Leaves'

    # S3 Bucket
    S3_BUCKET = 'f13-hrms-documents'

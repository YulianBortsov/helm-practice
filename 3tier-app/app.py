from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os

app = Flask(__name__)

# Database configuration from environment variables
DB_HOST = os.getenv('DATABASE_HOST', 'localhost')
DB_NAME = os.getenv('DATABASE_NAME', 'postgres')
DB_USER = os.getenv('DATABASE_USER', 'postgres')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD', 'password')

# SQLAlchemy database URI
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# SQLAlchemy engine
engine = create_engine(DATABASE_URI)

@app.route('/')
def check_db_connection():
    try:
        # Test connection by executing a simple query
        with engine.connect() as connection:
            result = connection.execute(text('SELECT 1;'))
            for _ in result:
                pass  # Just to fetch the result
        return jsonify({'status': 'success', 'message': 'Database connection is healthy!'})
    except SQLAlchemyError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

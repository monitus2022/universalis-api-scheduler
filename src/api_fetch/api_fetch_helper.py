import requests
from src.utils import logger
import csv


def fetch_api_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.info(
            f"Fetched content from {url} (status: {response.status_code}, time: {response.elapsed.total_seconds()}s)")
        return response.content
    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
        return None


def api_response_to_csv(content):
    try:
        decoded_content = content.decode('utf-8')
        csv_reader = csv.reader(decoded_content.splitlines(), delimiter=',')
        csv_data = list(csv_reader)
        logger.info(f"Converted API response to CSV format with {len(csv_data)} rows.")
        return csv_data
    except Exception as e:
        logger.error(f"Error converting API response to CSV: {e}")
        return None

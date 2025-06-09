from api_fetch_helper import *
from src.constants import *


class ApiFetchInfrequent:

    @staticmethod
    def fetch_and_convert():
        """
        Fetch content from the API and convert it to CSV format.

        :return: A list of lists representing the CSV data, or None if an error occurs.
        """
        url = item_info_csv_remote_path
        content = fetch_api_content(url)
        if content is None:
            return None
        return api_response_to_csv(content)


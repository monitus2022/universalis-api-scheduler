from api_fetch_helper import *


class ApiFetchInfrequent:

    @staticmethod
    def fetch_and_convert(url):
        """
        Fetch content from the API and convert it to CSV format.

        :param url: The API endpoint URL to fetch data from.
        :return: A list of lists representing the CSV data, or None if an error occurs.
        """
        content = fetch_api_content(url)
        if content is None:
            return None
        return api_response_to_csv(content)

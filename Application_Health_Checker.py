import requests
import logging

# Configure logging
logging.basicConfig(filename='app_health.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def check_app_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Application is up and running. Status code: {response.status_code}")
            print(f"Application is UP. Status code: {response.status_code}")
        else:
            logging.warning(f"Application is DOWN. Status code: {response.status_code}")
            print(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to reach application. Error: {str(e)}")
        print(f"Application is DOWN. Error: {str(e)}")

if __name__ == "__main__":
    app_url = "https://www.linkedin.com/in/adityagangil007/"
    check_app_status(app_url)

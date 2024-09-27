from abc import ABC, abstractmethod
import json
import requests

class Tariff(ABC):
    """
    Abstract base class for Tariff.
    """

    @abstractmethod
    def get_current_price(self):
        """
        Get the current price information.
        """
        pass

    @abstractmethod
    def get_prices(self):
        """
        Get the current price information.
        """
        pass

    @abstractmethod
    def get_today_prices(self):
        """
        Get today's price information.
        """
        pass

    @abstractmethod
    def get_tomorrow_prices(self):
        """
        Get tomorrow's price information.
        """
        pass



class Tibber(Tariff):
    def __init__(self, api_token):
        self.api_token = api_token
        self.api_url = 'https://api.tibber.com/v1-beta/gql'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_token}'
        }

    def _fetch_data(self, query):
        payload = {
            'query': query
        }
        response = requests.post(self.api_url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

    def get_current_price(self):
        query = """
        {
          viewer {
            homes {
              currentSubscription {
                priceInfo {
                  current {
                    total
                    energy
                    tax
                    startsAt
                  }
                }
              }
            }
          }
        }
        """
        data = self._fetch_data(query)
        return data['data']['viewer']['homes'][0]['currentSubscription']['priceInfo']['current']

    def get_prices(self):
      query = """
      {
        viewer {
          homes {
            currentSubscription {
              priceInfo {
                current {
                  total
                  energy
                  tax
                  startsAt
                }
                today {
                  total
                  energy
                  tax
                  startsAt
                }
                tomorrow {
                  total
                  energy
                  tax
                  startsAt
                }
              }
            }
          }
        }
      }
      """
      data = self._fetch_data(query)
      return data['data']['viewer']['homes'][0]['currentSubscription']['priceInfo']
    
    def get_today_prices(self):
        query = """
        {
          viewer {
            homes {
              currentSubscription {
                priceInfo {
                  today {
                    total
                    energy
                    tax
                    startsAt
                  }
                }
              }
            }
          }
        }
        """
        data = self._fetch_data(query)
        return data['data']['viewer']['homes'][0]['currentSubscription']['priceInfo']['today']

    def get_tomorrow_prices(self):
        query = """
        {
          viewer {
            homes {
              currentSubscription {
                priceInfo {
                  tomorrow {
                    total
                    energy
                    tax
                    startsAt
                  }
                }
              }
            }
          }
        }
        """
        data = self._fetch_data(query)
        return data['data']['viewer']['homes'][0]['currentSubscription']['priceInfo']['tomorrow']
from ./../abc import ApiFetcherBase

class DMIClient(ApiFetcherBase):
    """
    A concrete API client for the Danish Meteorological Institute (DMI).
    """
    DEFAULT_DMI_BASE_URL = "https://dmigw.govcloud.dk/metObs/v1"

    def __init__(self, api_key):
        # Call the parent's __init__
        super().__init__(api_key=api_key, base_url=self.DEFAULT_DMI_BASE_URL)
        print(f"DMIClient initialized for base URL: {self.base_url}")

    def fetch_data(self, endpoint: str, params: dict = None) -> dict:
        """
        Fetches data from a DMI API endpoint.
        Example endpoint: 'observation'
        Example params: {'stationId': '06180'}
        """
        if not self.base_url:
            raise ValueError("Base URL for DMI not set.")
        
        full_url = f"{self.base_url}/{endpoint.lstrip('/')}"
        print(f"Fetching data from DMI: {full_url} with params: {params}")
        
        # Using the helper method from the base class
        response = self._make_request("GET", full_url, params=params)
        return response.json()

    def get_service_status(self) -> str:
        # A specific implementation for DMI's status
        # This is a simplified example; a real one might ping a health check endpoint
        try:
            # Let's try fetching a known public, simple endpoint as a health check
            test_endpoint = "observation" # A common endpoint
            test_params = {'limit': 1, 'stationId': '06180'} # A minimal valid request
            full_url = f"{self.base_url}/{test_endpoint}"
            self._make_request("GET", full_url, params=test_params)
            return "DMI Service: Operational"
        except requests.exceptions.RequestException:
            return "DMI Service: Potentially Down or Unreachable"

# --- Let's try to use it ---
# dmi_api_key = "YOUR_DMI_API_KEY" # Replace with a real key if testing
# if dmi_api_key == "YOUR_DMI_API_KEY":
#     print("Please replace 'YOUR_DMI_API_KEY' with an actual API key to run DMI examples.")
# else:
#     dmi_fetcher = DMIClient(api_key=dmi_api_key)
#     print(dmi_fetcher.get_service_status())
#     dmi_fetcher.some_common_utility()
    # observations = dmi_fetcher.fetch_data(endpoint="observation", params={"stationId": "06180", "limit": 5})
    # print(f"Fetched {len(observations)} observations from DMI.")


# --- What happens if a subclass FORGETS to implement an abstract method? ---

class IncompleteFetcher(ApiFetcherBase):
    def __init__(self, api_key):
        super().__init__(api_key)

    def fetch_data(self, endpoint: str, params: dict = None) -> dict:
        # This one is implemented
        print(f"IncompleteFetcher fetching {endpoint} with {params}")
        return {"data": "some_data"}

    # OOPS! We forgot to implement get_service_status()

# Try to instantiate IncompleteFetcher:
try:
    bad_fetcher = IncompleteFetcher(api_key="dummy_key")
except TypeError as e:
    print(f"\nError instantiating IncompleteFetcher: {e}")
    # Expected output:
    # Error instantiating IncompleteFetcher: Can't instantiate abstract class IncompleteFetcher
    # with abstract method get_service_status
# datafetch/abc/ftp_fetcher.py
from abc import ABC, abstractmethod
from typing import List

class FtpFetcherBase(ABC):
    def __init__(self, host: str, username: str = None, password: str = None, port: int = 21, **kwargs):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ftp_connection = None # To be managed by connect/disconnect

    @abstractmethod
    def connect(self):
        """Establishes the FTP connection."""
        pass

    @abstractmethod
    def disconnect(self):
        """Closes the FTP connection."""
        pass

    @abstractmethod
    def list_directory(self, remote_path: str) -> List[str]:
        """Lists files and directories in a remote path."""
        pass

    @abstractmethod
    def download_file(self, remote_path: str, local_path: str) -> None:
        """Downloads a file from the FTP server."""
        pass

    @abstractmethod
    def get_service_status(self) -> str:
        """Checks the status/availability of the FTP service."""
        pass
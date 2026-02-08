for downloading lookup tabels we need a resolver that can resolve sg.lookup(dk.dar.foretningsgang) into fetching the table from thi github pages using somthing like this:
# lib/registry.py

class Namespace:
    def __init__(self, tld_code: str, github_repo: str):
        self.tld = tld_code
        self.base_url = f"https://raw.githubusercontent.com/{github_repo}/main/"

    def get_url(self, path: str) -> str:
        # Translates DAR.Forretningshændelse to the raw MD path
        return f"{self.base_url}{path.replace('.', '/')}.md"

# Pre-configured Top-Level Namespaces
dk = Namespace("dk", "Esbern/semanticgis-dk")
eu = Namespace("eu", "Esbern/semanticgis-eu")
G  = Namespace("G",  "Esbern/semanticgis-org")

def resolve_lookup(symbol_path: str):
    """
    The engine: Fetches the MD, parses the table, and returns a Dict.
    Includes a local cache check to prevent redundant web requests.
    """
    # 1. Check local ~/.semanticgis/cache/
    # 2. If not found, fetch from GitHub Raw
    # 3. Parse Markdown table -> Python Dict
    pass


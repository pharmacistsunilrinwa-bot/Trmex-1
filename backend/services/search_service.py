import os
from tavily import TavilyClient

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class SearchService:
    @staticmethod
    async def web_search(query: str):
        response = tavily.search(query=query, search_depth="advanced")
        return response['results']

search_service = SearchService()

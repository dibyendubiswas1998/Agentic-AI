from langchain_openai import AzureChatOpenAI
from typing import Union, Optional, Dict, Any
from dotenv import load_dotenv
import logging
import os
import certifi  

# Set SSL certificate path
os.environ['SSL_CERT_FILE'] = certifi.where()



# Load environment variables
load_dotenv()

# Load all AZURE related secrects
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

# Set the environment variables:
os.environ["AZURE_OPENAI_ENDPOINT"] = os.environ["AZURE_OPENAI_ENDPOINT"]


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class AzureOpenAIHandler:
    def __init__(self, 
                 azure_openai_endpoint:Optional[str]=None,
                 azure_openai_api_key:Optional[str]=None, 
                 azure_openai_version:Optional[str]=None,
                 azure_deployment_name:Optional[str]=None,
        ):
        """
            Initialize the Azure OpenAI handler.
        """
        self._endpoint = azure_openai_endpoint or AZURE_OPENAI_ENDPOINT
        self._api_key = azure_openai_api_key or AZURE_OPENAI_API_KEY        
        self._version = azure_openai_version or AZURE_API_VERSION
        self._deployment = azure_deployment_name or AZURE_DEPLOYMENT_NAME
        
        self._validate_environment()
    
    
    def _validate_environment(self) -> None:
        """Validate that required environment variables are set."""
        
        if not all([self._api_key, self._version, self._endpoint, self._deployment]): 
            raise ValueError("Missing required Azure OpenAI parameters: api_key, api_version, azure_endpoint, or deployment")
    
        
    def get_llm(self, temperature: Union[float, int]=0.9, **kwargs:Dict[str, Any]) -> AzureChatOpenAI:
        """
            Load the LLM from AZURE OPENAI ENDPOINT
        """
        import httpx
        
        # Create a custom client with SSL verification disabled
        client = httpx.Client(verify=False)
        
        try:
            # Validate parameters
            if not isinstance(temperature, (float, int)) or not 0 <= temperature <= 1:
                raise ValueError("Temperature must be between 0 and 1")
            
            logger.info(
                f"Initializing AzureChatOpenAI with model={self._deployment}, "
                f"temperature={temperature}"
            )
            
            # Return LLM: AzureChatOpenAI
            return AzureChatOpenAI(
                api_key=self._api_key,
                api_version=self._version,
                azure_deployment=self._deployment,
                temperature=temperature,
                http_client=client,
                **kwargs
            )
            
        except ValueError as ve:
            logger.error(f"Validation error in AzureOpenAIHandler get_llm method: {str(ve)}")
            raise
        
        except Exception as ex:
            logger.error(
                f"Error initializing AzureChatOpenAI with model {self._deployment}: {str(ex)}",
                exc_info=True
            )
            raise RuntimeError(
                f"Failed to initialize AzureChatOpenAI after retries: {str(ex)}"
            ) from ex
            
            

if __name__ == "__main__":
    # Usage example
    llm = AzureOpenAIHandler().get_llm()
    print(llm.invoke("Hello ji, kase ho?"))
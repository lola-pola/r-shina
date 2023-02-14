import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('Start Function APP')
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential , EnvironmentCredential #Import the required modules
        key = req.params.get('key') #Get the key to disable from the request
        kv_url = req.params.get('kv_url') #Get the key vault url to connect to from the request
        if kv_url == None:
            kv_url='https://toooo1234.vault.azure.net/' #If no key vault url is specified, use this one.
        credential = EnvironmentCredential() #Use the default credentials (use the environment variables for authentication)
        client = SecretClient(vault_url=kv_url, credential=credential) #Create the client
        if client.update_secret_properties(key, enabled=False): #Update the secret to disable it.
            return func.HttpResponse(f"changed.",status_code=200)
        else:
            return func.HttpResponse(f"ERROR.",status_code=500)


    except Exception as Error:
        return func.HttpResponse(f"ERROR, {Error}. is not allowed.",status_code=200)

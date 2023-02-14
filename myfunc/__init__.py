import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('Start Function APP')
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential , EnvironmentCredential
        key = req.params.get('key')
        kv_url = req.params.get('kv_url')
        if kv_url == None:
            kv_url='https://toooo1234.vault.azure.net/'
        credential = EnvironmentCredential()
        client = SecretClient(vault_url=kv_url, credential=credential)
        if client.update_secret_properties(key, enabled=False):
            return func.HttpResponse(f"changed.",status_code=200)
        else:
            return func.HttpResponse(f"ERROR.",status_code=500)


    except Exception as Error:
        return func.HttpResponse(f"ERROR, {Error}. is not allowed.",status_code=500)

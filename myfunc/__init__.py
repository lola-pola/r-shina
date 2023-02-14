import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('UP')

        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential , EnvironmentCredential
        enable_status = req.params.get('enable_status')
        key = req.params.get('key')
        logging.info('UP1')
        
        KVUri = f"https://toooo1234.vault.azure.net/"
        # credential = DefaultAzureCredential()
        credential = EnvironmentCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)
        client.update_secret_properties(key, enabled=True)
        return func.HttpResponse(f"changed.",status_code=200)
        # enable_status = bool(enable_status)
        # secretName= key
        # status= enable_status
        # KVUri = f"https://shuval.vault.azure.net/"
        # credential = DefaultAzureCredential()
        # client = SecretClient(vault_url=KVUri, credential=credential)
        # logging.info('UP2')

        # # print(f"Retrieving your secret from {secretName}.")
        # client.update_secret_properties(secretName, enabled=status)
        # if status:
        #     retrieved_secret = client.get_secret(secretName)
        #     print(f"Your secret vault is {retrieved_secret.value}")
        #     print(" done.")
        # else:
        #     print(f"Your secret status is {status} .")


        # return func.HttpResponse(f"DEBUG.",status_code=200)


    except Exception as Error:
        return func.HttpResponse(f"ERROR, {Error}. is not allowed.",status_code=200)


#test
import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('UP')
        from azure.keyvault.secrets import SecretClient
        logging.info('UP1')
        from azure.identity import DefaultAzureCredential
        logging.info('UP2')

        secretName='test'
        status= True
        KVUri = f"https://shuval.vault.azure.net/"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=KVUri, credential=credential)
        # print(f"Retrieving your secret from {secretName}.")
        # client.update_secret_properties(secretName, enabled=status
        # if status:
        #     retrieved_secret = client.get_secret(secretName)
        #     print(f"Your secret vault is '{retrieved_secret.value}
        #     print(" done.")
        # else:
        #     print(f"Your secret status is {status} .")
        
        
        return func.HttpResponse(f"DEBUG.",status_code=200)

        # credential = DefaultAzureCredential()
        # logging.info('UP')
        # from azure.keyvault.keys import KeyClient
        # key_client = KeyClient(vault_url="https://elhaysssss.vault.azure.net/", credential=credential)
        # logging.info('Python HTTP trigger function processed a request.')
        # allow_enable = ['eefrat']
        # enable_status = req.params.get('enable_status')
        # key = req.params.get('key')
        # username = req.params.get('username')
        # if username in allow_enable:
        #     updated_key = key_client.update_key_properties(key, enabled=True)
        #     print(updated_key.name)
        #     print(updated_key.properties.enabled)
        #     return func.HttpResponse(
        #          f"Hello, {username}. is not updated the keys.",
        #          status_code=200
        #     )
        # else:
        #     return func.HttpResponse(f"Hello, {username}. is not allowed.",
        #                                 status_code=401
        #     )
    except Exception as Error:
        return func.HttpResponse(f"ERROR, {Error}. is not allowed.",status_code=401)


#test
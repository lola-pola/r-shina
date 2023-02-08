import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('UP')
        logging.info('UP1')
        from azure.keyvault.secrets import SecretClient
        from azure.identity import DefaultAzureCredential
        enable_status = req.params.get('enable_status')
        key = req.params.get('key')
        username = req.params.get('username')
        if username == 'eefrat':
            return func.HttpResponse(f"changed.",status_code=200)
            enable_status = bool(enable_status)
            secretName= key
            status= enable_status
            KVUri = f"https://shuval.vault.azure.net/"
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url=KVUri, credential=credential)
            logging.info('UP2')

            # print(f"Retrieving your secret from {secretName}.")
            client.update_secret_properties(secretName, enabled=status)
            if status:
                retrieved_secret = client.get_secret(secretName)
                print(f"Your secret vault is {retrieved_secret.value}")
                print(" done.")
            else:
                print(f"Your secret status is {status} .")


            return func.HttpResponse(f"DEBUG.",status_code=200)
        else:
            return func.HttpResponse(f"Hello, {username}. is not allowed.",status_code=401)

    except Exception as Error:
        return func.HttpResponse(f"ERROR, {Error}. is not allowed.",status_code=200)


#test
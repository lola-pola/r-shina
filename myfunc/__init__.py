import logging
# from azure.identity import DefaultAzureCredential
# from azure.keyvault.keys import KeyClient
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    # try:
        # credential = DefaultAzureCredential()
        logging.info('UP')
        username = req.params.get('username')
        return func.HttpResponse(
                 f"Hello, {username}. is not updated the keys.",
                 status_code=200
            )
        # from azure.keyvault.keys import KeyClient
        # key_client = KeyClient(vault_url="https://elhaysssss.vault.azure.net/", credential=credential)
    #     logging.info('Python HTTP trigger function processed a request.')
    #     allow_enable = ['eefrat']
    #     enable_status = req.params.get('enable_status')
    #     key = req.params.get('key')
    #     username = req.params.get('username')
    #     if username in allow_enable:
    #         updated_key = key_client.update_key_properties(key, enabled=enable_status)
    #         print(updated_key.name)
    #         print(updated_key.properties.enabled)
    #         return func.HttpResponse(
    #              f"Hello, {username}. is not updated the keys.",
    #              status_code=200
    #         )
    #     else:
    #         return func.HttpResponse(f"Hello, {username}. is not allowed.",
    #                                     status_code=401
    #         )
    # except Exception as Error:
    #     return func.HttpResponse(f"ERROR, {Error}. is not allowed.",
    #                                     status_code=401

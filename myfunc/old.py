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
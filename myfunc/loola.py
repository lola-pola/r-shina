



def loola(secretName='test', status=True):
    from azure.keyvault.secrets import SecretClient
    from azure.identity import DefaultAzureCredential

    KVUri = f"https://shuval.vault.azure.net/"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)
    print(f"Retrieving your secret from {secretName}.")
    client.update_secret_properties(secretName, enabled=status)
    if status:
        retrieved_secret = client.get_secret(secretName)
        print(f"Your secret vault is '{retrieved_secret.value} is now {status} '.")
        print(" done.")
    else:
        print(f"Your secret status is {status} .")


loola()
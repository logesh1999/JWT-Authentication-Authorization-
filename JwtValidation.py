import jwt
from msal import JwtValidator
from azure.identity import DefaultAzureCredential


tenant_id = 'your-tenant-id'
audience = 'your-audience'
validator = JwtValidator(
    audience=[audience],
    issuers=[f'https://sts.windows.net/{tenant_id}/'],
    validate_exp=True
)


credential = DefaultAzureCredential()


token = 'your-jwt-token'
decoded_token = jwt.decode(token, verify=False)
claims = validator.get_validated_claims(token)


try:
    claims = validator.get_validated_claims(token)
except Exception as ex:
    print(f'Error validating JWT: {ex}')

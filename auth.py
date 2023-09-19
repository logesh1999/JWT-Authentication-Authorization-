import jwtfrom jwt.algorithms
import RSAAlgorithm
import requests
# Define the OpenID Connect metadata URL
metadata_url = f"https://login.microsoftonline.com/{tenant_id}/.well-known/openid-configuration"
# Retrieve the configuration data (including signing keys)
response = requests.get(metadata_url) 
jwks_uri = response.json()["jwks_uri"] 
jwks_response = requests.get(jwks_uri) 
jwks = jwks_response.json() 
signing_keys = [] 
for key in jwks["keys"]: 
    signing_key = RSAAlgorithm.from_jwk(key) 
    signing_keys.append(signing_key) 
    
    
# Define the parameters for token validation
validation_params = { 
    # Specify the valid issuer of the token (your Azure AD tenant) 
    "issuer": f"https://sts.windows.net/{tenant_id}/",
    # Specify the valid audience for the token (your API or resource) 
    "audience": "https://management.azure.com/",
      
    # Specify the signing key for the token 
    "algorithms": ["RS256"], 
    "verify_signature": True, 
    "issuer_signing_keys": signing_keys
    } 

# Validate the token and get the claims principal
try: 
    claims = jwt.decode(accessToken, options={"verify_signature": False}, algorithms=["RS256"]) 
    claims_principal = jwt.decode(accessToken, options=validation_params, algorithms=["RS256"]) 
    # Token is valid. You can now use the claims principal to authorize the user.
except jwt.exceptions.InvalidTokenError as ex: 
# Token validation failed
#  # Handle the exception as appropriate
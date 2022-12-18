from __future__ import print_function

import time
from pprint import pprint

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from infrastructure.core.config import settings

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = settings.SMTP_API_KEY

# create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration))


def send_new_account_email(email, username, code):
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": email, "name": username}],
        template_id=1,
        params={"full_name": username, "code": code}
    )

    # SendSmtpEmail | Values to send a transactional email

    try:
        # Send a transactional email
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)

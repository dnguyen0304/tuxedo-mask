# -*- coding: utf-8 -*-

import base64

from tuxedo_mask import clients, models


def create_authorization_header(username, password):

    encoded = base64.b64encode((username + ':' + password).encode('utf-8'))
    header = 'Basic ' + encoded.decode('utf-8')
    return header


tuxedo_mask_client = clients.TuxedoMaskClient.from_configuration()
authentication_client = clients.StormpathClient.from_configuration()

# Register / sign up Tuxedo Mask for an authentication service.
tuxedo_mask_application = tuxedo_mask_client.applications.get_by_name('tuxedo_mask')
# do you even need this feature? friggin thing doesn't create directories
# authentication_client.applications.add(entity=tuxedo_mask_application)

# Register / sign up a new "Applications" for Tuxedo Mask.
import uuid
username = str(uuid.uuid4())
mfit_user = models.Users(
    applications_id=tuxedo_mask_application.applications_id,
    username=username,
    password='Foobar12345!')

# tuxedo_mask_client.users.add(entity=mfit_user, by=tuxedo_mask_application)
# tuxedo_mask_client.commit()

authentication_client.users.add(entity=mfit_user)

# Authenticate an Application.
header = create_authorization_header(username=username,
                                     password='Foobar12345!')

print(authentication_client.verify_credentials(header=header,
                                         scope=tuxedo_mask_application))

# Authenticate an Application with the wrong password.
header = create_authorization_header(username=username,
                                     password='oobar12345!')

print(authentication_client.verify_credentials(header=header,
                                               scope=tuxedo_mask_application))

# Authenticate an Application that doesn't exist.
header = create_authorization_header(username='Foobar12345!',
                                     password='Foobar12345!')

print(authentication_client.verify_credentials(header=header,
                                               scope=tuxedo_mask_application))


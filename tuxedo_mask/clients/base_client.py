# -*- coding: utf-8 -*-

import abc
import base64

from tuxedo_mask import repositories


class BaseClient(repositories.UnitOfWork, metaclass=abc.ABCMeta):

    def __init__(self, db_context, repositories, logger):
        self._logger = logger
        super().__init__(repositories=repositories,
                         db_context=db_context,
                         logger=logger)

    @classmethod
    @abc.abstractmethod
    def from_configuration(cls):
        pass

    def verify_credentials(self, header, scope):

        """
        Parse the authorization header, decode the credentials, and
        then verify them.

        The header must be formatted according to the Basic Access
        Authentication scheme described in RFC 1945 [1] [2].

        Parameters
        ----------
        header : str
            Authentication scheme, and encoded username and password.
        scope : models.Applications
            Namespace within which to search for the user.

        Returns
        -------
        bool
            True if the username and password match those of an existing
            user's. False if the username matches that of an existing
            user's, but the password does not.

        Raises
        ------
        ValueError
            If the username does not match that of an existing user's.

        References
        ----------
        .. [1] Berners-Lee, et al., "Access Authentication",
           https://tools.ietf.org/html/rfc1945#section-11
        .. [2] Franks, et al., "Basic Authentication Scheme",
           https://tools.ietf.org/html/rfc2617#section-2
        """

        credentials = self._parse_authorization_header(header)
        return self._do_verify_credentials(*credentials, scope=scope)

    @staticmethod
    def _parse_authorization_header(header):

        """
        Returns
        -------
        tuple
            Decoded username and password. Two-element tuple of strings.
            The first element is the decoded username. The second
            element is the decoded, unhashed password.
        """

        encoded = header.split()[1]
        decoded = base64.b64decode(encoded.encode('utf-8')).decode('utf-8')
        username, password = decoded.split(':')
        return username, password

    @abc.abstractmethod
    def _do_verify_credentials(self, username, password, scope):
        pass


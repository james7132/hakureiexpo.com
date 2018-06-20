import endpoints
import httplib


class BaseServiceException(endpoints.ServiceException):

    @classmethod
    def raise_if_not_exists(cls, key):
        result = key.get()
        if result:
            msg = 'A {} for this ID does not exist. (ID: {})'.format(
                key.kind().lower(),
                key.id())
            raise cls(msg)
        return result

    @classmethod
    def raise_if_exists(cls, key):
        if key.get():
            msg = 'A {} has already been created. (ID: {})'.format(
                key.kind().lower(),
                key.id())
            raise cls(msg)


class NotFoundException(BaseServiceException):
    """Conflict exception that is mapped to a HTTP 404 response"""
    http_status = httplib.NOT_FOUND


class ConflictException(BaseServiceException):
    """Conflict exception that is mapped to a HTTP 409 response"""
    http_status = httplib.CONFLICT

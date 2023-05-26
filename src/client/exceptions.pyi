__all__ = [
    'SpecClassIdentificationError',
    'ApiError',
    'ValidationApiError',
    'InternalApiError',
    'AuthenticationApiError',
    'AccessDeniedApiError',
    'RemoteServiceUnavailableApiError',
    'DoesNotExistApiError',
    'ConflictStateApiError',
    'TooManyRequestsApiError',
    'IncorrectActionsApiError',
    'raise_on_api_error',
    'FailedOperation',
]
import httpx
import typing


class SpecClassIdentificationError(Exception):
    """An exception that is raised when a specification сlass can't be find for a field specification name.

    Attributes:
        spec_field: The field specification name.
        spec_enum: An enumeration with all known specification names.
    """

    def __init__(
        self,
        *,
        spec_field: typing.Optional[str] = None,
        spec_enum: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class SpecClassIdentificationError.
        """
        ...

    spec_field: typing.Optional[str]
    spec_enum: typing.Optional[str]


class FailedOperation(Exception):
    """An exception that is raised when an operation fails.

    It could be raised when an inner operation fails.

    Attributes:
        operation: The instance of the failed operation.
    """

    def __init__(self, *, operation: typing.Optional[typing.Any] = None) -> None:
        """Method generated by attrs for class FailedOperation.
        """
        ...

    operation: typing.Optional[typing.Any]


class ApiError(Exception):
    """A base class for exceptions that are raised when API methods return errors.

    Attributes:
        status_code: A HTTP response status code.
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
    """

    def __init__(
        self,
        *,
        request_id: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        payload: typing.Optional[typing.Any] = None,
        status_code: typing.Optional[int] = None,
        response: typing.Optional[httpx.Response] = None
    ) -> None:
        """Method generated by attrs for class ApiError.
        """
        ...

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


class ValidationApiError(ApiError):
    """An exception for a field validation error returned by an API method.

    Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
        invalid_fields: A list of invalid fields.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]
    _invalid_fields: typing.Optional[typing.List[str]]


class InternalApiError(ApiError):
    """Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


class AuthenticationApiError(ApiError):
    """Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


class AccessDeniedApiError(ApiError):
    """Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


class RemoteServiceUnavailableApiError(ApiError):
    """Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


class DoesNotExistApiError(ApiError):
    """Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


class ConflictStateApiError(ApiError):
    """Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


class TooManyRequestsApiError(ApiError):
    """Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


class IncorrectActionsApiError(ApiError):
    """Attributes:
        request_id: The ID of the request that returns an error.
        code: An error code.
        message: An error description.
        payload: Additional data describing an error.
        status_code: A HTTP response status code.
    """

    request_id: typing.Optional[str]
    code: typing.Optional[str]
    message: typing.Optional[str]
    payload: typing.Optional[typing.Any]
    status_code: typing.Optional[int]
    response: typing.Optional[httpx.Response]


def raise_on_api_error(response: httpx.Response): ...

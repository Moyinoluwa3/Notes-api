from src.exceptions import BadRequest, NotAuthenticated, PermissionDenied,NotFound


class ErrorCode:
    AUTHENTICATION_REQUIRED = "Authentication required."
    AUTHORIZATION_FAILED = "Authorization failed. User has no access."
    INVALID_TOKEN = "Invalid token."
    INVALID_CREDENTIALS = "Invalid credentials."
    EMAIL_TAKEN = "Email is already taken."
    TOKEN_NOT_VALID = "Refresh token is not valid."
    TOKEN_REQUIRED = "Refresh token is required either in the body or cookie."
    USER_NOT_FOUND = "This User was not Found"
    TOKEN_EXPIRED = "Token expired"


class AuthRequired(NotAuthenticated):
    DETAIL = ErrorCode.AUTHENTICATION_REQUIRED


class AuthorizationFailed(PermissionDenied):
    DETAIL = ErrorCode.AUTHORIZATION_FAILED


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class EmailTaken(BadRequest):
    DETAIL = ErrorCode.EMAIL_TAKEN


class TokenNotValid(NotAuthenticated):
    DETAIL = ErrorCode.TOKEN_NOT_VALID

class UserNotFound(NotFound):
     DETAIL = ErrorCode.USER_NOT_FOUND

class TokenExpired(NotAuthenticated):
    DETAIL = ErrorCode.TOKEN_EXPIRED
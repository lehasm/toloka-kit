__all__ = [
    'CommonErrorCodes',
    'InternalErrorCodes',
    'ValidationErrorCodes',
]
import enum


class CommonErrorCodes(enum.Enum):
    """Common error codes returned by Toloka.
    """

    ACCESS_DENIED = 'ACCESS_DENIED'
    AUTHENTICATION_ERROR = 'AUTHENTICATION_ERROR'
    CONFLICT_STATE = 'CONFLICT_STATE'
    DOES_NOT_EXIST = 'DOES_NOT_EXIST'
    INTERNAL_ERROR = 'INTERNAL_ERROR'
    REMOTE_SERVICE_UNAVAILABLE = 'REMOTE_SERVICE_UNAVAILABLE'
    TOO_MANY_REQUESTS = 'TOO_MANY_REQUESTS'
    VALIDATION_ERROR = 'VALIDATION_ERROR'


class InternalErrorCodes(enum.Enum):
    """Internal error codes returned by Toloka.
    """

    ACCOUNT_ALREADY_USED = 'ACCOUNT_ALREADY_USED'
    ACCOUNT_MUST_BE_IDENTIFIED = 'ACCOUNT_MUST_BE_IDENTIFIED'
    ADJUSTER_NOT_FOUND = 'ADJUSTER_NOT_FOUND'
    ALL_ASSIGNMENTS_EXHAUSTED = 'ALL_ASSIGNMENTS_EXHAUSTED'
    ASSIGNMENTS_AGGREGATION_DENIED = 'ASSIGNMENTS_AGGREGATION_DENIED'
    ASSIGNMENTS_COUNT_CONFLICT = 'ASSIGNMENTS_COUNT_CONFLICT'
    BATCH_INITIALIZATION_ERROR = 'BATCH_INITIALIZATION_ERROR'
    BATCH_REJECTED = 'BATCH_REJECTED'
    BILLING_NOT_SYNCHRONIZED = 'BILLING_NOT_SYNCHRONIZED'
    CAPTCHA_REQUIRED = 'CAPTCHA_REQUIRED'
    DELETE_ALL_TASKS_CONFLICT = 'DELETE_ALL_TASKS_CONFLICT'
    EMPTY_POOL = 'EMPTY_POOL'
    INAPPROPRIATE_STATUS = 'INAPPROPRIATE_STATUS'
    INCORRECT_RECIPIENTS = 'INCORRECT_RECIPIENTS'
    INVALID_OPERATION_TYPE = 'INVALID_OPERATION_TYPE'
    INVALID_REFERRAL_CODE = 'INVALID_REFERRAL_CODE'
    INVALID_WORKER_STATUS_ERROR = 'INVALID_WORKER_STATUS_ERROR'
    MIXER_CONFIG_REQUIRED = 'MIXER_CONFIG_REQUIRED'
    NEED_PHONE_CONFIRMATION = 'NEED_PHONE_CONFIRMATION'
    NOT_ENOUGH_BALANCE = 'NOT_ENOUGH_BALANCE'
    OAUTH_AUTHENTICATION_ERROR = 'OAUTH_AUTHENTICATION_ERROR'
    OPERATION_ALREADY_EXISTS = 'OPERATION_ALREADY_EXISTS'
    OPERATION_EXECUTION_ERROR = 'OPERATION_EXECUTION_ERROR'
    OPERATION_LOGS_ARCHIVED = 'OPERATION_LOGS_ARCHIVED'
    PAYONEER_ACCOUNT_NOT_ACTIVE = 'PAYONEER_ACCOUNT_NOT_ACTIVE'
    PAYPAL_AUTH_CODE_INVALID = 'PAYPAL_AUTH_CODE_INVALID'
    PAYPAL_UNVERIFIED_USER = 'PAYPAL_UNVERIFIED_USER'
    POOL_ASSIGNMENTS_COUNT_EXCEEDED = 'POOL_ASSIGNMENTS_COUNT_EXCEEDED'
    POOL_ASSIGNMENTS_EXHAUSTED = 'POOL_ASSIGNMENTS_EXHAUSTED'
    POOL_INAPPROPRIATE_STATUS = 'POOL_INAPPROPRIATE_STATUS'
    POOL_INVALID_FILTER_FOR_MAP_ISSUING = 'POOL_INVALID_FILTER_FOR_MAP_ISSUING'
    POOL_IS_TRAINING = 'POOL_IS_TRAINING'
    POOL_LOCKED_BY_ANOTHER_OPERATION = 'POOL_LOCKED_BY_ANOTHER_OPERATION'
    POOL_TASKS_COUNT_EXCEEDED = 'POOL_TASKS_COUNT_EXCEEDED'
    POOL_TASK_SUITES_COUNT_EXCEEDED = 'POOL_TASK_SUITES_COUNT_EXCEEDED'
    POOL_TASK_TYPE_CONFLICT = 'POOL_TASK_TYPE_CONFLICT'
    PROJECT_INAPPROPRIATE_STATUS = 'PROJECT_INAPPROPRIATE_STATUS'
    RESULTS_EXPIRED = 'RESULTS_EXPIRED'
    SECURE_PHONE_DUPLICATION = 'SECURE_PHONE_DUPLICATION'
    SECURE_PHONE_MISSING = 'SECURE_PHONE_MISSING'
    SECURE_PHONE_WAS_CHANGED = 'SECURE_PHONE_WAS_CHANGED'
    SKILL_IS_TRAINING = 'SKILL_IS_TRAINING'
    SKILL_IS_USED = 'SKILL_IS_USED'
    SKILL_IS_USED_BY_PROJECTS = 'SKILL_IS_USED_BY_PROJECTS'
    SKILL_REMOVED = 'SKILL_REMOVED'
    SUBMITTED_ASSIGNMENTS_CONFLICT = 'SUBMITTED_ASSIGNMENTS_CONFLICT'
    SYNC_POOL_CLONE_ERROR = 'SYNC_POOL_CLONE_ERROR'
    SYSTEM_SCOPE_MODIFICATION = 'SYSTEM_SCOPE_MODIFICATION'
    TASK_VALIDATION_ERROR = 'TASK_VALIDATION_ERROR'
    THERE_IS_ACTIVE_ASSIGNMENT = 'THERE_IS_ACTIVE_ASSIGNMENT'
    THERE_IS_REJECTED_ASSIGNMENT = 'THERE_IS_REJECTED_ASSIGNMENT'
    TOO_MANY_ACTIVE_ASSIGNMENTS = 'TOO_MANY_ACTIVE_ASSIGNMENTS'
    TRAINING_ARCHIVE_CONFLICT = 'TRAINING_ARCHIVE_CONFLICT'
    UNABLE_TO_UPLOAD_FILE = 'UNABLE_TO_UPLOAD_FILE'
    UNARCHIVED_POOLS_CONFLICT = 'UNARCHIVED_POOLS_CONFLICT'
    UNSUPPORTED_ALGORITHM = 'UNSUPPORTED_ALGORITHM'
    UNSUPPORTED_REGION = 'UNSUPPORTED_REGION'
    USER_ALREADY_REGISTERED = 'USER_ALREADY_REGISTERED'
    USER_HAS_PDD_ALIAS = 'USER_HAS_PDD_ALIAS'
    WITHDRAWAL_TRANSACTION_CANNOT_BE_CANCELLED = 'WITHDRAWAL_TRANSACTION_CANNOT_BE_CANCELLED'
    WITHDRAWAL_TRANSACTION_CANNOT_BE_CANCELLED_DUE_TO_TIME_LIMIT = 'WITHDRAWAL_TRANSACTION_CANNOT_BE_CANCELLED_DUE_TO_TIME_LIMIT'
    WORKER_SKILL_EXISTS = 'WORKER_SKILL_EXISTS'
    WRONG_FILE_FORMAT = 'WRONG_FILE_FORMAT'
    WRONG_REVISION = 'WRONG_REVISION'


class ValidationErrorCodes(enum.Enum):
    """Validation error codes returned by Toloka.
    """

    ARRAY_EXPECTED = 'ARRAY_EXPECTED'
    ARRAY_SIZE_GREATER_THAN_MAX = 'ARRAY_SIZE_GREATER_THAN_MAX'
    ARRAY_SIZE_LESS_THAN_MIN = 'ARRAY_SIZE_LESS_THAN_MIN'
    ARRAY_SIZE_OUT_OF_BOUNDS = 'ARRAY_SIZE_OUT_OF_BOUNDS'
    BLANK_STRING_NOT_ALLOWED = 'BLANK_STRING_NOT_ALLOWED'
    BOOLEAN_EXPECTED = 'BOOLEAN_EXPECTED'
    CHARACTER_NOT_ALLOWED = 'CHARACTER_NOT_ALLOWED'
    DATE_OUT_OF_RANGE = 'DATE_OUT_OF_RANGE'
    DUPLICATE_VALUE_IN_ARRAY = 'DUPLICATE_VALUE_IN_ARRAY'
    EMPTY_OBJECT_NOT_ALLOWED = 'EMPTY_OBJECT_NOT_ALLOWED'
    ENTITY_ACCESS_DENIED = 'ENTITY_ACCESS_DENIED'
    ENTITY_DOES_NOT_EXIST = 'ENTITY_DOES_NOT_EXIST'
    FLOAT_EXPECTED = 'FLOAT_EXPECTED'
    INTEGER_EXPECTED = 'INTEGER_EXPECTED'
    INVALID_COORDINATES_SYNTAX = 'INVALID_COORDINATES_SYNTAX'
    INVALID_DATE_SYNTAX = 'INVALID_DATE_SYNTAX'
    INVALID_DATE_TIME_SYNTAX = 'INVALID_DATE_TIME_SYNTAX'
    INVALID_REGEX_SYNTAX = 'INVALID_REGEX_SYNTAX'
    INVALID_URL_SYNTAX = 'INVALID_URL_SYNTAX'
    INVALID_VALUE = 'INVALID_VALUE'
    JSON_EXPECTED = 'JSON_EXPECTED'
    MAX_ONE_PROPERTY_ALLOWED = 'MAX_ONE_PROPERTY_ALLOWED'
    NAME_LENGTH_LESS_THAN_MIN = 'NAME_LENGTH_LESS_THAN_MIN'
    NOT_NULL_BODY = 'NOT_NULL_BODY'
    OBJECT_EXPECTED = 'OBJECT_EXPECTED'
    OBJECT_SIZE_BYTES_GREATER_THAN_MAX = 'OBJECT_SIZE_BYTES_GREATER_THAN_MAX'
    PATTERN_MISMATCH = 'PATTERN_MISMATCH'
    SIMPLE_VALUE_EXPECTED = 'SIMPLE_VALUE_EXPECTED'
    STRING_EXPECTED = 'STRING_EXPECTED'
    STRING_LENGTH_GREATER_THAN_MAX = 'STRING_LENGTH_GREATER_THAN_MAX'
    STRING_LENGTH_LESS_THAN_MIN = 'STRING_LENGTH_LESS_THAN_MIN'
    STRING_LENGTH_OUT_OF_BOUNDS = 'STRING_LENGTH_OUT_OF_BOUNDS'
    UNKNOWN_ENUM_VALUE = 'UNKNOWN_ENUM_VALUE'
    UUID_EXPECTED = 'UUID_EXPECTED'
    VALUES_REQUIRED = 'VALUES_REQUIRED'
    VALUE_GREATER_THAN_MAX = 'VALUE_GREATER_THAN_MAX'
    VALUE_LESS_THAN_MIN = 'VALUE_LESS_THAN_MIN'
    VALUE_NOT_ALLOWED = 'VALUE_NOT_ALLOWED'
    VALUE_OUT_OF_BOUNDS = 'VALUE_OUT_OF_BOUNDS'
    VALUE_REQUIRED = 'VALUE_REQUIRED'

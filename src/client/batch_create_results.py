__all__ = [
    'FieldValidationError',
    'TaskBatchCreateResult',
    'TaskSuiteBatchCreateResult',
    'UserBonusBatchCreateResult',
    'WebhookSubscriptionBatchCreateResult'
]
from typing import Any, Dict, List, Optional, Type

from .primitives.base import BaseTolokaObject, BaseTolokaObjectMetaclass
from .task import Task
from .task_suite import TaskSuite
from .user_bonus import UserBonus
from .webhook_subscription import WebhookSubscription


class FieldValidationError(BaseTolokaObject):
    """An error that contains information about an invalid field.

    Attributes:
        code: The error code.
        message: The error message.
        params: A list with additional parameters describing the error.
    """

    code: str
    message: str
    params: List[Any]


def _create_batch_create_result_class_for(type_: Type, docstring: Optional[str] = None):
    cls = BaseTolokaObjectMetaclass(
        f'{type_.__name__}BatchCreateResult',
        (BaseTolokaObject,),
        {
            'validation_errors': None,
            '__annotations__': {
                'items': Dict[str, type_],
                'validation_errors': Optional[Dict[str, Dict[str, FieldValidationError]]],
            }
        },
    )
    cls.__module__ = __name__
    cls.__doc__ = docstring
    return cls


TaskBatchCreateResult = _create_batch_create_result_class_for(
    Task,
    """The result of a task creation.

    `TaskBatchCreateResult` is returned by the [create_tasks](toloka.client.TolokaClient.create_tasks.md) method.

    Attributes:
        items: A dictionary with created tasks.
        validation_errors: A dictionary with validation errors in input tasks. It is filled if the request parameter `skip_invalid_items` is `True`.
    """
)
TaskSuiteBatchCreateResult = _create_batch_create_result_class_for(
    TaskSuite,
    """The result of a task suite creation.

    `TaskSuiteBatchCreateResult` is returned by the [create_task_suites](toloka.client.TolokaClient.create_task_suites.md) method.

    Attributes:
        items: A dictionary with created task suites.
        validation_errors: A dictionary with validation errors in input task suites. It is filled if the request parameter `skip_invalid_items` is `True`.
    """
)
UserBonusBatchCreateResult = _create_batch_create_result_class_for(
    UserBonus,
    """The result of issuing rewards for Tolokers.

    Attributes:
        items: A dictionary with created rewards.
        validation_errors: A dictionary with validation errors. It is filled if the request parameter `skip_invalid_items` is `True`.
    """
)
WebhookSubscriptionBatchCreateResult = _create_batch_create_result_class_for(
    WebhookSubscription,
    """The result of creating webhook subscriptions.

    Attributes:
        items: A dictionary with created subscriptions.
        validation_errors: A dictionary with validation errors.
    """
)

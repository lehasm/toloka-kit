__all__ = [
    'Attachment',
    'AssignmentAttachment',
]
import datetime
import toloka.client.owner
import toloka.client.primitives.base
import toloka.util._extendable_enum
import typing


class Attachment(toloka.client.primitives.base.BaseTolokaObject):
    """An attachment.

    Files attached to tasks by Tolokers are uploaded to Toloka.

    Attributes:
        id: The file ID.
        name: The file name.
        details: Attachment details: a pool, task, and Toloker who uploaded the file.
        created: The date and time when the file was uploaded.
        media_type: The file [MIME](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) data type.
        owner: The owner of the attachment.
    """

    class Type(toloka.util._extendable_enum.ExtendableStrEnum):
        """An enumeration.
        """

        ASSIGNMENT_ATTACHMENT = 'ASSIGNMENT_ATTACHMENT'

    class Details(toloka.client.primitives.base.BaseTolokaObject):
        """Attachment details.

        Attributes:
            user_id: The ID of the Toloker who attached the file.
            assignment_id: The ID of the assignment with the file.
            pool_id: The ID of the pool.
        """

        def __init__(
            self,
            *,
            user_id: typing.Optional[str] = None,
            assignment_id: typing.Optional[str] = None,
            pool_id: typing.Optional[str] = None
        ) -> None:
            """Method generated by attrs for class Attachment.Details.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        user_id: typing.Optional[str]
        assignment_id: typing.Optional[str]
        pool_id: typing.Optional[str]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[Details] = None,
        created: typing.Optional[datetime.datetime] = None,
        media_type: typing.Optional[str] = None,
        owner: typing.Optional[toloka.client.owner.Owner] = None
    ) -> None:
        """Method generated by attrs for class Attachment.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    id: typing.Optional[str]
    name: typing.Optional[str]
    details: typing.Optional[Details]
    created: typing.Optional[datetime.datetime]
    media_type: typing.Optional[str]
    owner: typing.Optional[toloka.client.owner.Owner]


class AssignmentAttachment(Attachment):
    """An attachment to an assignment.

    Attributes:
        id: The file ID.
        name: The file name.
        details: Attachment details: a pool, task, and Toloker who uploaded the file.
        created: The date and time when the file was uploaded.
        media_type: The file [MIME](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) data type.
        owner: The owner of the attachment.

    Examples:
        >>> attachment = toloka_client.get_attachment(attachment_id='0983459b-e26f-42f3-a5fd-6e3feee913e7')
        >>> print(attachment.id, attachment.name)
        ...
    """

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        details: typing.Optional[Attachment.Details] = None,
        created: typing.Optional[datetime.datetime] = None,
        media_type: typing.Optional[str] = None,
        owner: typing.Optional[toloka.client.owner.Owner] = None
    ) -> None:
        """Method generated by attrs for class AssignmentAttachment.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    id: typing.Optional[str]
    name: typing.Optional[str]
    details: typing.Optional[Attachment.Details]
    created: typing.Optional[datetime.datetime]
    media_type: typing.Optional[str]
    owner: typing.Optional[toloka.client.owner.Owner]

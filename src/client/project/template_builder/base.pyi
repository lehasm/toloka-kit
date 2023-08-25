__all__ = [
    'ComponentType',
    'BaseTemplateMetaclass',
    'BaseTemplate',
    'BaseComponent',
    'BaseComponentOr',
    'base_component_or',
    'VersionedBaseComponentMetaclass',
    'UnknownComponent',
    'RefComponent',
    'ListDirection',
    'ListSize',
]
import toloka.client.primitives.base
import toloka.util._extendable_enum
import typing


class ComponentType(toloka.util._extendable_enum.ExtendableStrEnum):
    """An enumeration.
    """

    ACTION_BULK = 'action.bulk'
    ACTION_NOTIFY = 'action.notify'
    ACTION_OPEN_CLOSE = 'action.open-close'
    ACTION_OPEN_LINK = 'action.open-link'
    ACTION_PLAY_PAUSE = 'action.play-pause'
    ACTION_ROTATE = 'action.rotate'
    ACTION_SET = 'action.set'
    ACTION_TOGGLE = 'action.toggle'
    CONDITION_ALL = 'condition.all'
    CONDITION_ANY = 'condition.any'
    CONDITION_EMPTY = 'condition.empty'
    CONDITION_EQUALS = 'condition.equals'
    CONDITION_LINK_OPENED = 'condition.link-opened'
    CONDITION_NOT = 'condition.not'
    CONDITION_PLAYED = 'condition.played'
    CONDITION_PLAYED_FULLY = 'condition.played-fully'
    CONDITION_REQUIRED = 'condition.required'
    CONDITION_SAME_DOMAIN = 'condition.same-domain'
    CONDITION_SCHEMA = 'condition.schema'
    CONDITION_SUB_ARRAY = 'condition.sub-array'
    CONDITION_YANDEX_DISTANCE = '@yandex-toloka/condition.distance'
    DATA_INPUT = 'data.input'
    DATA_INTERNAL = 'data.internal'
    DATA_LOCAL = 'data.local'
    DATA_LOCATION = '@yandex-toloka/data.location'
    DATA_OUTPUT = 'data.output'
    DATA_RELATIVE = 'data.relative'
    FIELD_AUDIO = 'field.audio'
    FIELD_BUTTON_RADIO = 'field.button-radio'
    FIELD_BUTTON_RADIO_GROUP = 'field.button-radio-group'
    FIELD_CHECKBOX = 'field.checkbox'
    FIELD_CHECKBOX_GROUP = 'field.checkbox-group'
    FIELD_DATE = 'field.date'
    FIELD_EMAIL = 'field.email'
    FIELD_FILE = 'field.file'
    FIELD_IMAGE_ANNOTATION = 'field.image-annotation'
    FIELD_LIST = 'field.list'
    FIELD_MEDIA_FILE = 'field.media-file'
    FIELD_NUMBER = 'field.number'
    FIELD_PHONE_NUMBER = 'field.phone-number'
    FIELD_RADIO_GROUP = 'field.radio-group'
    FIELD_SELECT = 'field.select'
    FIELD_TEXT = 'field.text'
    FIELD_TEXT_ANNOTATION = 'field.text-annotation'
    FIELD_TEXTAREA = 'field.textarea'
    HELPER_CONCAT_ARRAYS = 'helper.concat-arrays'
    HELPER_ENTRIES2OBJECT = 'helper.entries2object'
    HELPER_IF = 'helper.if'
    HELPER_JOIN = 'helper.join'
    HELPER_OBJECT2ENTRIES = 'helper.object2entries'
    HELPER_REPLACE = 'helper.replace'
    HELPER_SEARCH_QUERY = 'helper.search-query'
    HELPER_SWITCH = 'helper.switch'
    HELPER_TEXT_TRANSFORM = 'helper.text-transform'
    HELPER_TRANSFORM = 'helper.transform'
    HELPER_TRANSLATE = 'helper.translate'
    HELPER_YANDEX_DISK_PROXY = '@yandex-toloka/helper.proxy'
    LAYOUT_BARS = 'layout.bars'
    LAYOUT_COLUMNS = 'layout.columns'
    LAYOUT_COMPARE = 'layout.compare'
    LAYOUT_SIDE_BY_SIDE = 'layout.side-by-side'
    LAYOUT_SIDEBAR = 'layout.sidebar'
    PLUGIN_IMAGE_ANNOTATION_HOTKEYS = 'plugin.field.image-annotation.hotkeys'
    PLUGIN_TEXT_ANNOTATION_HOTKEYS = 'plugin.field.text-annotation.hotkeys'
    PLUGIN_HOTKEYS = 'plugin.hotkeys'
    PLUGIN_TRIGGER = 'plugin.trigger'
    PLUGIN_TOLOKA = 'plugin.toloka'
    VIEW_ACTION_BUTTON = 'view.action-button'
    VIEW_ALERT = 'view.alert'
    VIEW_AUDIO = 'view.audio'
    VIEW_COLLAPSE = 'view.collapse'
    VIEW_DEVICE_FRAME = 'view.device-frame'
    VIEW_DIVIDER = 'view.divider'
    VIEW_GROUP = 'view.group'
    VIEW_IFRAME = 'view.iframe'
    VIEW_IMAGE = 'view.image'
    VIEW_LABELED_LIST = 'view.labeled-list'
    VIEW_LINK = 'view.link'
    VIEW_LINK_GROUP = 'view.link-group'
    VIEW_LIST = 'view.list'
    VIEW_MAP = 'view.map'
    VIEW_MARKDOWN = 'view.markdown'
    VIEW_TEXT = 'view.text'
    VIEW_VIDEO = 'view.video'


class BaseTemplateMetaclass(toloka.client.primitives.base.BaseTolokaObjectMetaclass):
    @staticmethod
    def __new__(
        mcs,
        *args,
        kw_only=False,
        **kwargs
    ): ...


class BaseTemplate(toloka.client.primitives.base.BaseTolokaObject, metaclass=BaseTemplateMetaclass):
    @classmethod
    def structure(cls, data: dict): ...

    def __init__(self) -> None:
        """Method generated by attrs for class BaseTemplate.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]


class BaseComponent(BaseTemplate):
    @classmethod
    def structure(cls, data: dict): ...

    def __init__(self) -> None:
        """Method generated by attrs for class BaseComponent.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]


class BaseComponentOr(toloka.client.primitives.base.BaseTolokaObject):
    @classmethod
    def structure(cls, data): ...

    def __init__(self) -> None:
        """Method generated by attrs for class BaseComponentOr.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]


def base_component_or(type_: typing.Type, class_name_suffix: typing.Optional[str] = None): ...


class VersionedBaseComponentMetaclass(BaseTemplateMetaclass):
    def _validate_v1(
        self,
        attribute,
        value: str
    ) -> str: ...

    @staticmethod
    def __new__(
        mcs,
        name,
        bases,
        namespace,
        **kwargs
    ): ...


class UnknownComponent(BaseTemplate):
    def __init__(self) -> None:
        """Method generated by attrs for class UnknownComponent.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]


class RefComponent(BaseTemplate):
    """A reference to a component.

    Pass to the `RefComponent` constructor a path in the Template Builder component hierarchy.

    For more information, see [Reuse code](https://toloka.ai/docs/template-builder/best-practices/reuse).

    Example:
        >>> from toloka.client.project.template_builder import *
        >>>
        >>> tb_config = TemplateBuilder(
        >>>     vars = {
        >>>         '0' : InputData('question'),
        >>>         '1' : OutputData('answer')
        >>>     },
        >>>     view = TextFieldV1(
        >>>         data = RefComponent('vars.1'),
        >>>         label = RefComponent('vars.0')
        >>>     )
        >>> )
        ...
    """

    def __init__(self, ref: typing.Optional[str] = None) -> None:
        """Method generated by attrs for class RefComponent.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    ref: typing.Optional[str]


class ListDirection(toloka.util._extendable_enum.ExtendableStrEnum):
    """An enumeration.
    """

    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'


class ListSize(toloka.util._extendable_enum.ExtendableStrEnum):
    """An enumeration.
    """

    M = 'm'
    S = 's'

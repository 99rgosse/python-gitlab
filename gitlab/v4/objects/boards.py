from gitlab.base import *  # noqa
from gitlab.mixins import *  # noqa


__all__ = [
    "GroupBoardList",
    "GroupBoardListManager",
    "GroupBoard",
    "GroupBoardManager",
    "ProjectBoardList",
    "ProjectBoardListManager",
    "ProjectBoard",
    "ProjectBoardManager",
]


class GroupBoardList(SaveMixin, ObjectDeleteMixin, RESTObject):
    pass


class GroupBoardListManager(CRUDMixin, RESTManager):
    _path = "/groups/%(group_id)s/boards/%(board_id)s/lists"
    _obj_cls = GroupBoardList
    _from_parent_attrs = {"group_id": "group_id", "board_id": "id"}
    _create_attrs = (("label_id",), tuple())
    _update_attrs = (("position",), tuple())


class GroupBoard(SaveMixin, ObjectDeleteMixin, RESTObject):
    _managers = (("lists", "GroupBoardListManager"),)


class GroupBoardManager(CRUDMixin, RESTManager):
    _path = "/groups/%(group_id)s/boards"
    _obj_cls = GroupBoard
    _from_parent_attrs = {"group_id": "id"}
    _create_attrs = (("name",), tuple())


class ProjectBoardList(SaveMixin, ObjectDeleteMixin, RESTObject):
    pass


class ProjectBoardListManager(CRUDMixin, RESTManager):
    _path = "/projects/%(project_id)s/boards/%(board_id)s/lists"
    _obj_cls = ProjectBoardList
    _from_parent_attrs = {"project_id": "project_id", "board_id": "id"}
    _create_attrs = (("label_id",), tuple())
    _update_attrs = (("position",), tuple())


class ProjectBoard(SaveMixin, ObjectDeleteMixin, RESTObject):
    _managers = (("lists", "ProjectBoardListManager"),)


class ProjectBoardManager(CRUDMixin, RESTManager):
    _path = "/projects/%(project_id)s/boards"
    _obj_cls = ProjectBoard
    _from_parent_attrs = {"project_id": "id"}
    _create_attrs = (("name",), tuple())

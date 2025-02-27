from datetime import datetime
from typing import List

from pydantic import BaseModel


class CreatedBy(BaseModel):
    created: str = ""
    email: str = ""
    id: int = 0
    name: str = ""
    updated: str = None
    username: str = None


class File(BaseModel):
    created: str
    id: str
    mime: str
    name: str
    size: int


class Assignees(BaseModel):
    created: str
    email: str
    id: str
    name: str
    updated: str
    username: str


class Attachments(BaseModel):
    created: str
    created_by: CreatedBy
    file: File
    id: int
    task_id: int


class Buckets(BaseModel):
    count: int
    created: str
    created_by: CreatedBy
    id: int
    limit: int
    position: int
    project_view_id: int
    tasks: list
    title: str
    updated: str


class Author(BaseModel):
    created: str
    email: str
    id: int
    name: str
    updated: str
    username: str


class Comments(BaseModel):
    author: Author
    comment: str
    created: str
    id: int
    reactions: list  # Нужно доработать !!!!!
    updated: str


class Labels(BaseModel):
    created: str
    created_by: CreatedBy
    description: str
    hex_color: str
    id: int
    title: str
    updated: str


class Reactions(BaseModel):
    pass


class RelatedTasks(BaseModel):
    pass


class Reminders(BaseModel):
    pass


class Subscription(BaseModel):
    pass


class CreateTask(BaseModel):
    assignees: List[Assignees] = []
    attachments: List[Attachments] = []
    bucket_id: int = 0
    buckets: List[Buckets] = []
    comments: List[Comments] = []
    cover_image_attachment_id: int = None
    created: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    created_by: CreatedBy = {}
    description: str = ""
    done: bool = False
    done_at: str = None
    due_date: str = None
    end_date: str = None
    hex_color: str = ""
    id: int = 0
    identifier: str = ""
    index: int = 0
    is_favorite: bool = False
    labels: List[Labels] = []
    percent_done: int = 0
    position: int = 0
    priority: int = 0
    project_id: int = 0
    reactions: Reactions = {}
    related_tasks: RelatedTasks = {}
    reminders: List[Reminders] | None = []
    repeat_after: int = 0
    repeat_mode: int = 0
    start_date: str = None
    subscription: Subscription = None
    title: str = ""
    updated: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

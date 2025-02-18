from pydantic import BaseModel
from typing import List


class CreatedBy(BaseModel):
    created: str
    email: str
    id: int
    name: str
    updated: str
    username: str


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
    created: str = ""
    created_by: CreatedBy
    description: str = ""
    done: bool = False
    done_at: str = ""
    due_date: str = ""
    end_date: str = ""
    hex_color: str = ""
    id: int = 0
    identifier: str = 0
    index: int
    is_favorite: bool
    labels: List[Labels]
    percent_done: int
    position: int
    priority: int
    project_id: int
    reactions: Reactions
    related_tasks: RelatedTasks
    reminders: List[Reminders]
    repeat_after: int
    repeat_mode: int
    start_date: str
    subscription: Subscription
    title: str
    updated: str

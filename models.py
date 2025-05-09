from __future__ import annotations

from typing import Any
from datetime import datetime
from pydantic import BaseModel, model_validator


################################################################################
# Base
################################################################################

class Model(BaseModel):

    @model_validator(mode='before')
    @classmethod
    def convert_str(cls, data: Any) -> dict:
        if not isinstance(data, dict):
            return data

        for field, value in dict(data).items():
            if value is None:
                continue

            if cls.__annotations__.get(field) == str:
                data[field] = str(value)

        return data


################################################################################
# Title
################################################################################

class Title(Model):
    id: str
    title: str
    description: str


################################################################################
# Image
################################################################################

class Image(Model):
    id: str
    url: str


################################################################################
# Content
################################################################################

class TextBlock(Model):
    id: str
    content: str


class QuizzBlock(Model):
    id: str
    question: str
    answers: list[str]
    correct_answer: str


class Content(Model):
    id: str
    title: str
    description: str
    image_id: str | None
    created_at: datetime
    updated_at: datetime


class TextContent(Content):
    blocks: list[TextBlock]


class QuizzContent(Content):
    blocks: list[QuizzBlock]

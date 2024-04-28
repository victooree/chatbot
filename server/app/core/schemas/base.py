from datetime import datetime
from typing import Type, TypeVar
from tortoise import Model

from pydantic import BaseModel, ConfigDict

from server.app.utils.datetime import datetime_to_iso_format

T = TypeVar('T', bound=BaseModel)


class TortoiseORMSupportMixin:
    @classmethod
    def from_tortoise_orm(cls: Type[T], model_obj: Model) -> T:
        model_dict = dict(model_obj)

        for field_name in model_obj._meta.fetch_fields:
            if field_name in cls.__annotations__:
                value = getattr(model_obj, field_name)
                nested_pydantic_cls = cls.__fields__[field_name].annotation

                if isinstance(value, Model):
                    model_dict[field_name] = nested_pydantic_cls.from_tortoise_orm(value)
                else:
                    model_dict[field_name] = value

        return cls(**model_dict)


class ChatbotModel(TortoiseORMSupportMixin, BaseModel):
    model_config = ConfigDict(
        json_encoders={datetime: datetime_to_iso_format},
        from_attributes=True,
    )

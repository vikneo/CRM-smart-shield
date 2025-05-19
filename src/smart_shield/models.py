from datetime import datetime
from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import TEXT, Boolean, DateTime, Integer, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Project(db.Model):  # type: ignore
    """
    Класс описывает выпускаемый продукт с полями
    crm_id = CRM ID;
    company = Компания заказчик;
    project_name = Название проекта;
    slug = поле Slug по названию проекта;
    created_at = Дата создания;
    updated_at = Дата изменения;
    description = Описание проекта (не обязательно);
    archive = Архивация проекта (тип bool: True or False) при удалении
    """

    __tablename__ = "projects"
    __table_args__ = (
        UniqueConstraint(
            "slug",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    crm_id: Mapped[int] = mapped_column(Integer)
    company: Mapped[str] = mapped_column(String(80))
    project_name: Mapped[str] = mapped_column(String(80))
    slug: Mapped[str] = mapped_column(String(80), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime())
    description: Mapped[Optional[str]] = mapped_column(TEXT())
    archive: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self) -> str:
        return f"{self.crm_id}"

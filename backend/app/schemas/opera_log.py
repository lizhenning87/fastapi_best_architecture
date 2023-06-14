#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import BaseModel


class OperaLogBase(BaseModel):
    username: str | None = None
    method: str
    title: str
    path: str
    ip: str
    country: str | None = None
    region: str | None = None
    city: str | None = None
    user_agent: str
    os: str | None = None
    browser: str | None = None
    device: str | None = None
    args: dict | None = None
    status: bool
    code: int | str
    msg: str | None = None
    cost_time: float
    opera_time: datetime


class CreateOperaLog(OperaLogBase):
    pass


class UpdateOperaLog(OperaLogBase):
    pass


class GetAllOperaLog(OperaLogBase):
    id: int
    create_time: datetime

    class Config:
        orm_mode = True

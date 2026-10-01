"""Эмулятор командной оболочки ОС.

модуль содержит ...
"""

import getpass
import socket

def parse(l):
  com = []
  cur = []
  qt = None
  for ch in l:
    if qt is None:
      if ch in ("'", '"'):
        qt=ch
      elif ch.isspace():
        if cur:
          com.append("".join(cur))
          cur = []
      else:
        cur.append(ch)
    elif ch == qt:
      qt = None
    else:
      cur.append(ch)
  if qt is not None:
    raise ValueError("unclosed quote")
  if cur:
    com.append("".join(cur))
  if not com:
    return None, []
  return com[0], com[1:]

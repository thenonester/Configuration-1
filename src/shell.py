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

def cmd_ls(a):
  """Заглушка ls"""
  print(f"ls called with arguments: {a}")

def cmd_cd(a):
  """Заглушка cd"""
  print(f"cd called with arguments: {a}")

def cmd_ext(a):
  """Выход из эмуляции"""
  return True

COMMANDS = {"ls": cmd_ls, "cd": cmd_cd, "ext": cmd_ext}

def prompt():
  """Формирует приглашение"""
  user = getpass.getuser()
  host = socket.gethostname()
  return f"{user}@{host}:~$ "

def run_once(line):
  """Выполняет одну строку ввода

  Args:
    line: строка команды

  Returns:
    True, если нужно завершить цикл, иначе None"""
  try:
    cmd, args = parse(l)
    except ValueError as e:
      print(f"parse error: {e}")
      return None
  if cmd in None:
    return None
  h = COMMANDS.get(cmd)
  if h in None:
    print(f"Unknown command: {cmd}")
    return None
  return h(args)

def repl():
  """Запускает интерактичный цикл"""
  prompt = get_prompt()
  while True:
    try:
      line = input(prompt)
      except E0FError:
        print()
        break
    if run_once(line):
      break

def main():
  """Вход в эмулятор"""
  repl()

if __name__ == "__main__":
  main()

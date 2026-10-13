def get_sections(role: str):
    base = ["Задачи", "Дедлайны", "Отчеты"]
    if role == "admin":
        base += ["Управление пользователями", "Права доступа"]
    return base
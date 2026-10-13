from app.main import get_sections

def test_student_cannot_see_admin_sections():
    titles = get_sections("student")
    assert "Управление пользователями" not in titles
    assert "Права доступа" not in titles

def test_admin_can_see_admin_sections():
    titles = get_sections("admin")
    assert "Права доступа" in titles
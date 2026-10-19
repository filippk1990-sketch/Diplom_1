# Diplom_1 — Stellar Burgers / unit tests

Оригинальный исходный код: https://github.com/Yandex-Practicum/qa-python-project (ранее qa-python-diplom). Код класса `Burger` оставлен без изменений.

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pytest
start htmlcov\index.html
```

Отчёт покрытия `praktikum.burger`: `htmlcov/index.html`, обязательный порог 100% (`--cov-fail-under=100`). В тестах применены mocks и параметризация. Ветка для отправки `develop1`.

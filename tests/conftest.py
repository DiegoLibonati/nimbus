import tkinter as tk

import pytest


@pytest.fixture(scope="session")
def root() -> tk.Tk:
    instance: tk.Tk = tk.Tk()
    instance.withdraw()
    yield instance
    instance.destroy()


@pytest.fixture(scope="session")
def blank_photo(root: tk.Tk) -> tk.PhotoImage:
    return tk.PhotoImage(width=1, height=1)

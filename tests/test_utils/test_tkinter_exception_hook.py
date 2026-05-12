from unittest.mock import MagicMock, patch

from src.utils.dialogs import InternalDialogError, ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


class TestTkinterExceptionHook:
    def test_calls_open_on_base_dialog_instance(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="Test error")
        with patch.object(exc, "open") as mock_open:
            tkinter_exception_hook(type(exc), exc, None)
            mock_open.assert_called_once()

    def test_wraps_non_dialog_exception_in_internal_error(self) -> None:
        exc: ValueError = ValueError("something went wrong")
        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_cls:
            mock_instance: MagicMock = MagicMock()
            mock_cls.return_value = mock_instance
            tkinter_exception_hook(type(exc), exc, None)
            mock_cls.assert_called_once_with(message="something went wrong")
            mock_instance.open.assert_called_once()

    def test_internal_error_receives_exception_message(self) -> None:
        exc: RuntimeError = RuntimeError("runtime failure")
        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_cls:
            mock_cls.return_value = MagicMock()
            tkinter_exception_hook(type(exc), exc, None)
            mock_cls.assert_called_once_with(message="runtime failure")

    def test_internal_dialog_error_also_calls_open(self) -> None:
        exc: InternalDialogError = InternalDialogError(message="Internal")
        with patch.object(exc, "open") as mock_open:
            tkinter_exception_hook(type(exc), exc, None)
            mock_open.assert_called_once()

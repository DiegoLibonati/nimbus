from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message_is_app_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message_is_stored(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Custom error")
        assert dialog.message == "Custom error"

    def test_none_message_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)
        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.title == "Error"

    def test_to_dict_contains_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "dialog_type" in result

    def test_to_dict_contains_title(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "title" in result

    def test_to_dict_contains_message(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "message" in result

    def test_to_dict_correct_values(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Test message")
        result: dict[str, Any] = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["title"] == "Error"
        assert result["message"] == "Test message"

    def test_open_calls_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Test")
        mock_fn: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_fn}):
            dialog.open()
            mock_fn.assert_called_once_with("Error", "Test")


class TestBaseDialogError:
    def test_is_exception(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, Exception)

    def test_is_base_dialog(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert error.dialog_type == BaseDialog.ERROR


class TestValidationDialogError:
    def test_default_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError()
        assert error.message == "Validation error"

    def test_custom_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="Invalid input")
        assert error.message == "Invalid input"

    def test_is_raiseable(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError()

    def test_is_base_dialog_error(self) -> None:
        error: ValidationDialogError = ValidationDialogError()
        assert isinstance(error, BaseDialogError)


class TestAuthenticationDialogError:
    def test_default_message(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError()
        assert error.message == "Authentication error"

    def test_custom_message(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError(message="Unauthorized")
        assert error.message == "Unauthorized"

    def test_is_raiseable(self) -> None:
        with pytest.raises(AuthenticationDialogError):
            raise AuthenticationDialogError()


class TestNotFoundDialogError:
    def test_default_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError()
        assert error.message == "Resource not found"

    def test_custom_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError(message="Location not found")
        assert error.message == "Location not found"

    def test_is_raiseable(self) -> None:
        with pytest.raises(NotFoundDialogError):
            raise NotFoundDialogError()


class TestConflictDialogError:
    def test_default_message(self) -> None:
        error: ConflictDialogError = ConflictDialogError()
        assert error.message == "Conflict error"

    def test_is_raiseable(self) -> None:
        with pytest.raises(ConflictDialogError):
            raise ConflictDialogError()


class TestBusinessDialogError:
    def test_default_message(self) -> None:
        error: BusinessDialogError = BusinessDialogError()
        assert error.message == "Business rule violated"

    def test_is_raiseable(self) -> None:
        with pytest.raises(BusinessDialogError):
            raise BusinessDialogError()


class TestInternalDialogError:
    def test_default_message(self) -> None:
        error: InternalDialogError = InternalDialogError()
        assert error.message == "Internal error"

    def test_custom_message(self) -> None:
        error: InternalDialogError = InternalDialogError(message="Service down")
        assert error.message == "Service down"

    def test_is_raiseable(self) -> None:
        with pytest.raises(InternalDialogError):
            raise InternalDialogError()


class TestDeprecatedDialogWarning:
    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.message == "This feature is deprecated"

    def test_title_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.title == "Warning"

    def test_open_calls_showwarning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        mock_fn: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_fn}):
            warning.open()
            mock_fn.assert_called_once()


class TestSuccessDialogInformation:
    def test_dialog_type_is_info(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.message == "Operation completed successfully"

    def test_title_is_information(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.title == "Information"

    def test_open_calls_showinfo(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        mock_fn: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_fn}):
            info.open()
            mock_fn.assert_called_once()

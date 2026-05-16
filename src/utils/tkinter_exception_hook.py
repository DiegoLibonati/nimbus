# import traceback
import types

from src.configs.logger_config import setup_logger
from src.utils.dialogs import BaseDialog, InternalDialogError

logger = setup_logger("nimbus - tkinter_exception_hook")


def tkinter_exception_hook(
    exc_type: type[BaseException],
    exc_value: BaseException,
    exc_tb: types.TracebackType | None,
) -> None:
    # error_detail: str = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    # logger.error("Unhandled exception:\n%s", error_detail)

    if isinstance(exc_value, BaseDialog):
        exc_value.open()
    else:
        InternalDialogError(message=str(exc_value)).open()

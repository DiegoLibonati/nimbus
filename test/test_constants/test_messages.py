from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE,
    MESSAGE_NOT_FOUND_API_KEY,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_FOUND_LOCATION,
    MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE,
    MESSAGE_NOT_VALID_LOCATION,
)


class TestMessages:
    def test_error_app_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)

    def test_error_app_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_APP) > 0

    def test_error_geocoding_service_unavailable_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE, str)

    def test_error_geocoding_service_unavailable_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE) > 0

    def test_not_valid_latitude_and_longitude_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE, str)

    def test_not_valid_latitude_and_longitude_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE) > 0

    def test_not_valid_location_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_LOCATION, str)

    def test_not_valid_location_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_LOCATION) > 0

    def test_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_not_found_dialog_type_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0

    def test_not_found_location_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_LOCATION, str)

    def test_not_found_location_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_FOUND_LOCATION) > 0

    def test_not_found_api_key_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_API_KEY, str)

    def test_not_found_api_key_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_FOUND_API_KEY) > 0

    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            MESSAGE_ERROR_APP,
            MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE,
            MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE,
            MESSAGE_NOT_VALID_LOCATION,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
            MESSAGE_NOT_FOUND_LOCATION,
            MESSAGE_NOT_FOUND_API_KEY,
        ]
        assert len(all_messages) == len(set(all_messages))

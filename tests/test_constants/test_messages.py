from src.constants import messages


class TestMessages:
    def test_message_error_app_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_ERROR_APP, str)

    def test_message_error_app_not_empty(self) -> None:
        assert len(messages.MESSAGE_ERROR_APP) > 0

    def test_message_error_geocoding_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE, str)

    def test_message_error_geocoding_not_empty(self) -> None:
        assert len(messages.MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE) > 0

    def test_message_not_valid_lat_lon_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE, str)

    def test_message_not_valid_location_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_LOCATION, str)

    def test_message_not_found_dialog_type_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_message_not_found_location_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_FOUND_LOCATION, str)

    def test_message_not_found_api_key_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_FOUND_API_KEY, str)

    def test_all_messages_not_empty(self) -> None:
        all_messages: list[str] = [
            messages.MESSAGE_ERROR_APP,
            messages.MESSAGE_ERROR_GEOCODING_SERVICE_UNAVAILABLE,
            messages.MESSAGE_NOT_VALID_LATITUDE_AND_LONGITUDE,
            messages.MESSAGE_NOT_VALID_LOCATION,
            messages.MESSAGE_NOT_FOUND_DIALOG_TYPE,
            messages.MESSAGE_NOT_FOUND_LOCATION,
            messages.MESSAGE_NOT_FOUND_API_KEY,
        ]
        for msg in all_messages:
            assert len(msg) > 0

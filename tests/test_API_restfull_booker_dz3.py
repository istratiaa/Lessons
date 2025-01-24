from constant import BASE_URL


class TestBookings:

    # delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
    # assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
    #
    # get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
    # assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_get_booking(self, auth_session, booking_id):
        get_booking = auth_session.get(f"{BASE_URL}/booking")
        assert get_booking.status_code == 200
        assert [book_id["bookingid"] for book_id in get_booking.json() if book_id["bookingid"] == booking_id][
                   0] == booking_id, "созданый bookingid не найден"

    def test_put_booking(self, auth_session, booking_id, put_booking_data):
        get_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=put_booking_data)
        assert get_booking.status_code == 200

        booking_data_response1 = get_booking.json()
        assert booking_data_response1['firstname'] == put_booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response1['lastname'] == put_booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response1['totalprice'] == put_booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response1['depositpaid'] == put_booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response1['bookingdates']['checkin'] == put_booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response1['bookingdates']['checkout'] == put_booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

    def test_patch_booking(self, auth_session, booking_data, booking_id, patch_booking_data):
        get_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=patch_booking_data)
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == patch_booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == patch_booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == patch_booking_data['totalprice'], "Цена не совпадает с заданной"

    def test_delete_booking(self, auth_session, booking_id):
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

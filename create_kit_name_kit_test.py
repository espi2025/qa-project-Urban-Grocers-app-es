import data
import sender_stand_request

def positive_assert(kit_body):
    new_user = sender_stand_request.post_new_user(data.user_body)
    token = new_user.json().get('authToken')
    new_kit = sender_stand_request.create_kit(kit_body, token)
    assert new_kit.status_code == 201
    assert new_kit.json()["name"] == kit_body["name"]

def negative_assert(kit_body):
    new_user = sender_stand_request.post_new_user(data.user_body)
    token = new_user.json().get('authToken')
    new_kit = sender_stand_request.create_kit(kit_body, token)
    assert new_kit.status_code == 400
    assert new_kit.json()["code"] == 400
    assert new_kit.json()["message"] == "No se han aprobado todos los parámetros requeridos. " \
                                         "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def test_create_kit_name_one_letter_response_201():
    positive_assert(data.kit_body1)

def test_create_kit_name_511_letter_response_201():
    positive_assert(data.kit_body511)

def test_create_kit_name_0_letter_response_400():
    negative_assert(data.kit_body0)

def test_create_kit_name_512_letter_response_400():
    negative_assert(data.kit_body512)

def test_create_kit_name_especial_character_response_201():
    positive_assert(data.kit_body5)

def test_create_kit_name_space_allowed_response_201():
    positive_assert(data.kit_body6)

def test_create_kit_name_numbers_allowed_passed_response_201():
    positive_assert(data.kit_body7)

def test_create_kit_name_parameters_not_passed_response_400():
    negative_assert(data.kit_body8)

def test_create_kit_name_different_parameter_type_passed_response_400():
    negative_assert(data.kit_body9)
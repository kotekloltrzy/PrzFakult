#1.Wykonaj poniższe czynności:
#
#    Utwórz obiekt Mock i nadaj mu nazwę
#    Ustaw wartość zwracaną dla metody get_data
#    Wywołaj metodę get_data z argumentem user
#    Sprawdź czy metoda została wywołana używając assert_called_with
#    Sprawdź argumenty wywołania używając atrybutu call_args

from unittest.mock import Mock

my_mock = Mock(name='MyMock')

mock_obj = Mock(autospec=True)

my_mock.get_data.return_value = 'dane_testowe'

my_mock.get_data.assert_called_with('user')


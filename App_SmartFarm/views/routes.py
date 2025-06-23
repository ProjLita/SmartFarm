from views.Router import Router, DataStrategyEnum
from views.tela_main import IndexView
from views.plantacao import ProfileView
from views.settings_view import BluetoothView
from views.smartfarm1 import smartfarm1

router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": IndexView,
  "/plantacao": ProfileView,
  "/settings": BluetoothView,
  "/smartfarm1": smartfarm1
}
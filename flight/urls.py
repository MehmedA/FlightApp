from rest_framework.routers import DefaultRouter
from .views import PassengerView, ReservationsView, FlightView

router = DefaultRouter()
router.register('flight', FlightView)
router.register('reservations', ReservationsView)
router.register('passenger', PassengerView)

urlpatterns = router.urls

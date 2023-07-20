from rest_framework import routers
from .api import AddAvatarViewSet, AddDirectorViewSet, AddMovieViewSet, AddPlanetViewSet, AddProductorViewSet, AvatarViewSet, MoviesViewSet

router = routers.DefaultRouter()

router.register('api/avatar', AvatarViewSet, 'avatar')
router.register('api/addmovie', AddMovieViewSet, 'addmovie')
router.register('api/addavatar', AddAvatarViewSet, 'addavatar')
router.register('api/addplanet', AddPlanetViewSet, 'addplanet')

router.register('api/productor', AddProductorViewSet, 'productor')
router.register('api/director', AddDirectorViewSet, 'director')

urlpatterns = router.urls

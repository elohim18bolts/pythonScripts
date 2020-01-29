import views.home

class HomeController(object):

    def loadView(self):
        return views.home.homeView()
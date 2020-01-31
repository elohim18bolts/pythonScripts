import flaskApp.views.home as homeView

class HomeController(object):

    def loadView(self):
        return homeView.homeView()
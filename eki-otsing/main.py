
import cgi, os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import poomine

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {
            'count_results': '0',
            'results': '',
            'query': ''
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


class Tulemused(webapp.RequestHandler):
    def post(self):
        query = cgi.escape(self.request.get('query'))
        hangman = self.request.get('hangman')
        
        if hangman == '1':
            checked = 'checked'
        else:
            hangman = 0
            checked = ''
        count_results, results = poomine.main(query,hangman)
        template_values = {
            'count_results': count_results,
            'results': results,
            'query': query,
            'checked': checked
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))



application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/otsi', Tulemused)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
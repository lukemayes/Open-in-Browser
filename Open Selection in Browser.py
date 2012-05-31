import sublime, sublime_plugin
import webbrowser, re
from urlparse import urlparse

class OpenSelectionInBrowserCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            selection = self.view.substr(sel)
            webbrowser.open_new(urlparse(re.sub(r'\n|\r|\t|( ){2,}', '', selection)).geturl())

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

import logging
import requests

logger = logging.getLogger(__name__)

class RubyGemsExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        max_gems = 10
        query = event.get_argument()
        gems = requests.get("https://rubygems.org/api/v1/search/autocomplete", params = { "query": query }).json()
        items = [
            ExtensionResultItem(icon='images/icon.png',
                                         name=f'{gem} gem',
                                         description=f'https://rubygems.org/gems/{gem}',
                                         on_enter=OpenUrlAction(f'https://rubygems.org/gems/{gem}'))
            for gem in gems[:max_gems]
        ]

        return RenderResultListAction(items)

if __name__ == '__main__':
    RubyGemsExtension().run()

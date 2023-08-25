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
        items = []
        gems = []
        query = event.get_argument()
        response = requests.get("https://rubygems.org/api/v1/search/autocomplete", params = { "query": query })
        gems = response.json()
        for gem in gems:
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name=f'{gem} gem',
                                             description=f'https://rubygems.org/gems/{gem}',
                                             on_enter=OpenUrlAction(f'https://rubygems.org/gems/{gem}')))

        return RenderResultListAction(items)

if __name__ == '__main__':
    RubyGemsExtension().run()

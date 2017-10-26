import os

from pathlib import Path
from .base import Base

class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'minisnip'
        self.mark = '[minisnip]'
        self.min_pattern_length = 0
        self.snippets = os.listdir(str(Path.home()) + '/.vim/minisnip')

    def gather_candidates(self, context):
        """Returns all snippets in the users
        vim minisnip directory"""
        cleaned = [snippet.split('_')[2] for snippet in self.snippets if context['filetype'] in snippet]
        return [{'word': snippet} for snippet in cleaned]

import os

from pathlib import Path
from .base import Base

class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'minisnip'
        self.mark = '[minisnip]'
        self.min_pattern_length = 0
        self.minisnip_dir = self.vim.eval('g:minisnip_dir')
        self.snippets = os.listdir(self.minisnip_dir)

    def gather_candidates(self, context):
        """Returns all snippets in the users
        vim minisnip directory"""
        filetype = context['filetype']
        cleaned = [snippet.split('_' + filetype + '_')[1] for snippet in self.snippets if filetype in snippet]
        return [{'word': snippet} for snippet in cleaned]

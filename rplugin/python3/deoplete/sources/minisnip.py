from .base import Base

class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'minisnip'
        self.mark = '[minisnip]'
        self.min_pattern_length = 0

    def gather_candidates(self, context):
        return self.vim.call('minisnip#ListSnippets', context['input'])

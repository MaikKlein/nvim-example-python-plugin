import neovim

@neovim.plugin
class Limit(object):
    def __init__(self, vim):
        self.vim = vim
        self.calls = 0

    @neovim.command('HelloWorld', range='', nargs='*', sync=True)
    def hello_world_handler(self, args, range):
        self.vim.command('echo \"Hello World\"')

    @neovim.command('Cmd', range='', nargs='*', sync=True)
    def command_handler(self, args, range):
        self._increment_calls()
        self.vim.current.line = (
            'Command: Called %d times, args: %s, range: %s' % (self.calls,
                                                               args,
                                                               range))

    @neovim.autocmd('BufEnter', pattern='*.py', eval='expand("<afile>")',
                    sync=True)
    def autocmd_handler(self, filename):
        self._increment_calls()
        self.vim.current.line = (
            'Autocmd: Called %s times, file: %s' % (self.calls, filename))

    @neovim.function('Func')
    def function_handler(self, args):
        self._increment_calls()
        self.vim.current.line = (
            'Function: Called %d times, args: %s' % (self.calls, args))

    def _increment_calls(self):
        if self.calls == 5:
            raise Exception('Too many calls!')
        self.calls += 1

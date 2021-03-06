'''

Created on May 5, 2015

@author: jrosner
@last updated: 
component for running samtools index
'''

from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    def __init__(self,component_name='run_samtools_index', component_parent_dir=None, seed_dir=None):
        self.version = '1.0.0'
        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def focus(self, cmd, cmd_args, chunk):
        pass

    def make_cmd(self,chunk):
        cmd = self.requirements['samtools']

        cmd_args = ['index', self.args.input]

        return cmd, cmd_args

    def test(self):
        import component_test
        component_test.run()

def _main():
    comp = Component()
    comp.args = component_ui.args
    comp.run()
    comp.test()


if __name__ == '__main__':
    import component_ui
    _main()

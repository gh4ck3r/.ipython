import IPython.core.magic as ipym

@ipym.magics_class
class GccMagics(ipym.Magics):
    @ipym.cell_magic
    def cpp(self, line, cell=None):
        """ Compile, execute C++ code, and return the standard output."""
        from tempfile import NamedTemporaryFile
        with NamedTemporaryFile(mode="w", suffix=".cpp") as source:
            source.write(cell)
            source.flush()
            from os import path, unlink
            executable = path.splitext(source.name)[0]+'.exe'
            # Compile the C++ code into an executable with g++.
            compile = self.shell.getoutput(
                "g++ {0:s} -o {1:s}".format(source.name, executable))
            # Execute the executable and retrn the output.
            output = self.shell.getoutput(executable)
            unlink(executable)
            print output.n
            return output
        return None
    @ipym.cell_magic
    def foo(self, line, cell=None):
        help(self.shell.getoutput)

def load_ipython_extension(ipython):
    ipython.register_magics(GccMagics)

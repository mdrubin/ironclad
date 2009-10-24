
from tests.utils.runtest import makesuite, run
from tests.utils.testcase import TestCase

from System import IntPtr

from Ironclad.Structs import METH, PyMethodDef


class PythonStructsTest(TestCase):

    def testConstructPyMethodDef(self):
        pmd = PyMethodDef(
            "jennifer",
            IntPtr.Zero,
            METH.VARARGS,
            "jennifer's docs"
        )
        self.assertEquals(pmd.ml_name, "jennifer", "field not remembered")
        self.assertEquals(pmd.ml_meth, IntPtr.Zero, "field not remembered")
        self.assertEquals(pmd.ml_flags, METH.VARARGS, "field not remembered")
        self.assertEquals(pmd.ml_doc, "jennifer's docs", "field not remembered")


suite = makesuite(PythonStructsTest)

if __name__ == '__main__':
    run(suite)
from core.swmm.options.files import Files
from core.swmm.options import files
import unittest

class OptionsFilesTest(unittest.TestCase):
    def __init__(self):
        unittest.TestCase.__init__(self)
        self.my_options = Files()

    def setUp(self):

        self.my_options = files.Files()


    def runTest(self):

        name = self.my_options.SECTION_NAME
        assert name == "[FILES]"

        #20160407xw: if default, all nones, therefore no text
        actual_text = self.my_options.get_text()
        assert actual_text == ""

        #20160407xw: if all assigned with a file name, text in [:19]\t format
        #This test would fail because dictionary is not sorted.
        expected_text = "[FILES]\n" + \
                        ";;Interfacing Files\n" + \
                        " USE RAINFALL       \tuse_rainfall\n" + \
                        " SAVE RAINFALL      \tsave_rainfall\n" + \
                        " USE RUNOFF         \tuse_runoff\n" + \
                        " SAVE RUNOFF        \tsave_runoff\n" + \
                        " USE HOTSTART       \tuse hotstart\n" + \
                        " SAVE HOTSTART      \tsave_hotstart\n" + \
                        " USE RDII           \tuse_rdii\n" + \
                        " SAVE RDII	         \tsave_rdii\n" + \
                        " USE INFLOWS        \tuse_inflows\n" + \
                        " SAVE OUTFLOWS	     \tsave_outflows"

        self.my_options.use_rainfall =  "use_rainfall"
        self.my_options.save_rainfall = "save_rainfall"
        self.my_options.use_runoff = "use_runoff"
        self.my_options.save_runoff = "save_runoff"
        self.my_options.use_hotstart = "use_hotstart"
        self.my_options.save_hotstart = "save_hotstart"
        self.my_options.use_rdii = "use_rdii"
        self.my_options.save_rdii = "save_rdii"
        self.my_options.use_inflows = "use_inflows"
        self.my_options.save_outflows = "save_outflows"

        actual_text = self.my_options.get_text()
        assert actual_text == expected_text

        #20160407xw: if some with nones

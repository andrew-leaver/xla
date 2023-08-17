from xla.build_tools.github_actions.check_contents import check_contents
from xla.build_tools.github_actions.check_contents import diff_parser
class CheckDiffsTest(absltest.TestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    base_path = "third_party/xla/build_tools/github_actions/check_contents"
    with open(f"{base_path}/testdata/bad_cc.diff") as f:
      cls.bad_cc_hunks = diff_parser.parse_hunks(f.read())
    with open(f"{base_path}/testdata/important_cc.diff") as f:
      cls.important_cc_hunks = diff_parser.parse_hunks(f.read())
        self.bad_cc_hunks,
        prohibited_regex="Make_Unique",
        suppression_regex="OK",
        self.bad_cc_hunks, prohibited_regex="Make_Unique"
    filtered_hunks = check_contents.filter_hunks_by_path(
        self.bad_cc_hunks,
    self.assertLen(filtered_hunks, 1)
        filtered_hunks, prohibited_regex="Make_Unique"
    filtered_hunks = check_contents.filter_hunks_by_path(
        self.bad_cc_hunks,
    self.assertLen(filtered_hunks, 1)
        filtered_hunks, prohibited_regex="Make_Unique"
    filtered_hunks = check_contents.filter_hunks_by_path(
        self.bad_cc_hunks, path_regexes=[], path_regex_exclusions=[]
    self.assertEqual(self.bad_cc_hunks, filtered_hunks)
        filtered_hunks, prohibited_regex="Make_Unique", suppression_regex="OK"
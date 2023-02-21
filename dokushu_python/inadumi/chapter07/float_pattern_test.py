import regexp_test_tool as regtest

ok_list = [ "1", "+2", "-3", "12", "+23", "-34", "1897197", "+719871", "-188947"]
ng_list = [ "1.234a", "23.4568.901", "++1.23", "--52.23", "31.33-", "88.38--", "12..34"]

float_pattern = r"^(\+|-)?\d+(\.\d+)?$"

regtest.test(float_pattern, ok_list, True)
regtest.test(float_pattern, ng_list, False)
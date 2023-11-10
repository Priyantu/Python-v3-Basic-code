import re
pattern = r"[0-9][a-z][A-Z]"#কোন সেটের রেঞ্জ এর ভেতর কিছু আছে কিনা তাও চেক করা যায়
#মাল্টিপল সেট ও ব্যবহার করা যায়
if re.match(pattern,"0aEanhfeou"):
    print("Matched")
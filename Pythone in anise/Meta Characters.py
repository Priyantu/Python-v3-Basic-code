import re
pattern = r"a{1,3}$"#সর্বোচ্চ কয়টি থেকে কয়টি পর্যন্ত রাখতে পারবে তা দেখানোর জন্য
if re.match(pattern,"aaa"):
    print("Matched")

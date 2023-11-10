match = re.search(pattern,text)
if match:
    print(match.start())#প্যাটার্নের শুরু দেখার জন্য
    print(match.end())#প্যাটার্নের শেষ দেখার জন্য
    print(match.span())#প্যাটার্নের শুরু শেষ দুটোই দেখার জন্য  
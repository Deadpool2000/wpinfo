from wpinfo import WPInfo

site = WPInfo("https://example.wordpress.com")
info = site.get_info()

for key, value in info.items():
    print(f"{key.capitalize()}: {value}")

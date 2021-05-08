def number_to_letter(n):
    d_n = n // 26
    s_n = n % 26
    def ntl_chr(i):
        if 0< i <= 26:
            return  chr(i + 64)
        else:
            return  ""

    return ntl_chr(d_n) + ntl_chr(s_n)


def utf8_to_url_encode(s: str):
    import urllib
    s_url = urllib.parse.quote(s, encoding="utf-8", errors="replace")
    return s_url


def url_to_utf8_to_decode(s: str):
    import urllib
    s_url = urllib.parse.unquote(s, errors="replace")
    return s_url


def to_str_elif_empty_to_None(s):
    if not s:
        return None
    else:
        return str(s)

def to_int_elif_empty_to_None(s):
    if not s:
        return None
    else:
        return int(s)


from hashlib import md5


def encode_md5(text):
    return md5(text.encode("utf-8")).hexdigest()

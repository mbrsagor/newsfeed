def make_url(root_url, api, key):
    return f"{root_url}{api}{key}"


def validate_country(attrs):
    if "name" in attrs and len(attrs.get("owner")) < 1:
        return "name field is required"
    else:
        return True

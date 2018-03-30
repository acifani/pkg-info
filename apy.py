import requests


class Package(object):
    def __init__(self, data: dict):
        info: dict = data.get('info')
        self.raw_data: dict = data
        self.name: str = info.get('name')
        self.license: str = info.get('license')
        self.summary: str = info.get('summary')
        self.description: str = info.get('description')
        self.version: str = info.get('version')
        self.keywords: str = info.get('keywords')
        self.homepage: str = info.get('homepage')
        self.url: str = info.get('package_url')
        self.maintainer: Maintainer = Maintainer(
            info.get('maintainer'), info.get('maintainer_email'))
        self.author: Maintainer = Maintainer(
            info.get('author'), info.get('author_email'))

    def __repr__(self):
        return f'<Package name:"{self.name}" version:"{self.version}">'


class Maintainer(object):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


def _get_data(pkg_name: str) -> dict:
    url = f'https://pypi.python.org/pypi/{pkg_name}/json'
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def get_pkg_info(pkg_name: str) -> Package:
    data = _get_data(pkg_name)
    return Package(data) if data is not None else None

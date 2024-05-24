import sys
import types
from functools import lru_cache

from ._datastore import JSON


@lru_cache
def _get_datastore():
    from ._datastore import DataStore

    return DataStore()


class DataStoreProxy(types.ModuleType):
    """
    `DataStoreProxy` acts as a dynamic interface for interacting with various types of
    data stores within the `Automizor Platform`. It provides a convenient way to access
    and manipulate data stored in JSON and Key-Key-Value (KKV) formats.

    This class leverages the `Automizor DataStore` module to fetch and update data,
    utilizing a caching mechanism to enhance performance. The primary interaction is
    through attribute access and assignment, making it simple to work with different
    data structures.

    Example usage:

        .. code-block:: python

            from automizor import datastore

            # Initialize or update json store
            datastore.countries = [
                {
                    "name": "United States",
                    "code": "US",
                },
                {
                    "name": "Canada",
                    "code": "CA",
                },
            ]

            # Get values from json store
            countries = datastore.countries()

            # Initialize or update kkv store
            datastore.movies = {
                "US": {
                    "action": {
                        "Die Hard": 1988,
                        "The Matrix": 1999
                    }
                }
            }

            # Get values from kkv store
            movies = datastore.movies("US")
            movies_action = datastore.movies("US", "action")

            # Insert or update values
            datastore.movies = {
                "US": {
                    "action": {
                        "Die Hard": 1988,
                        "The Matrix": 1999,
                        "John Wick": 2014
                    },
                    "comedy": {
                        "The Hangover": 2009,
                        "Superbad": 2007
                    }
                }
            }

            # Delete secondary key
            datastore.movies = {
                "US": {
                    "action": None
                }
            }

            # Delete primary key
            datastore.movies = {
                "US": None
            }

    """

    def __getattr__(self, name):
        datastore = _get_datastore()

        def wrapper(primary_key=None, secondary_key=None):
            return datastore.get_values(name, primary_key, secondary_key)

        return wrapper

    def __setattr__(self, name, values: JSON):
        datastore = _get_datastore()
        datastore.set_values(name, values)


sys.modules[__name__] = DataStoreProxy(__name__)

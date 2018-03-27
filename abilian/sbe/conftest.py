# coding=utf-8
"""Configuration and injectable fixtures for Pytest.

Supposed to replace the too-complex current UnitTest-based testing
framework.

DI and functions over complex inheritance hierarchies FTW!
"""
from __future__ import absolute_import, division, print_function, \
    unicode_literals

from pytest import fixture

from abilian.conftest import TestConfig

from abilian.sbe.app import create_app
from abilian.services import get_service


# Change to True to enable errors on warnings
if True:
    import warnings
    # Do not remove !
    import pandas
    from sqlalchemy.exc import SADeprecationWarning
    warnings.simplefilter("ignore", SADeprecationWarning)
    warnings.simplefilter("ignore", FutureWarning)
    warnings.simplefilter("ignore", DeprecationWarning)
    # warnings.simplefilter("error")


@fixture
def app():
    return create_app(config=TestConfig)


@fixture
def db(app):
    """Return a fresh db for each test."""
    from abilian.core.extensions import db

    with app.app_context():
        stop_all_services(app)
        ensure_services_started(['repository', 'session_repository'])

        cleanup_db(db)
        db.create_all()
        yield db

        db.session.remove()
        cleanup_db(db)
        stop_all_services(app)


@fixture
def client(app, db):
    """Return a Web client, used for testing, bound to a DB session."""
    return app.test_client()


#
# Cleanup utilities
#
def cleanup_db(db):
    """Drop all the tables, in a way that doesn't raise integrity errors."""

    # Need to run this sequence twice for some reason
    delete_tables(db)
    delete_tables(db)
    # Just in case ?
    db.drop_all()


def delete_tables(db):
    for table in reversed(db.metadata.sorted_tables):
        try:
            db.session.execute(table.delete())
        except BaseException:
            pass


def stop_all_services(app):
    for service in app.services.values():
        if service.running:
            service.stop()


def ensure_services_started(services):
    for service_name in services:
        service = get_service(service_name)
        if not service.running:
            service.start()

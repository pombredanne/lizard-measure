#!/usr/bin/python
# -*- coding: utf-8 -*-

# pylint: disable=C0111

# Copyright (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

from django.core.management.base import BaseCommand

from lizard_measure.models import EsfPattern
from lizard_measure.models import MeasureType
from lizard_measure.models import WatertypeGroup

PATTERNS = [
    ['M','X','?','?','?','?','?','?','?','?','BR01'],
    ['M','X','?','?','?','?','?','X','?','?','BR04'],
    ['M','X','?','?','?','?','?','-','?','?','IM01'],
    ['M','X','?','?','?','?','X','?','?','?','IM03'],
    ['M','X','?','?','?','?','-','?','?','?','IM04'],
    ['M','X','?','?','?','?','?','?','?','?','IM05'],
    ['M','X','?','?','?','?','?','X','?','?','IM06'],
    ['M','X','?','?','?','?','?','-','?','?','IM08'],
    ['M','X','?','?','?','?','X','?','?','?','IM09'],
    ['M','X','?','?','?','?','-','?','?','?','IN01'],
    ['M','X','?','?','?','?','?','?','?','?','IN02'],
    ['M','X','?','?','?','?','?','X','?','?','IN03'],
    ['M','X','?','?','?','?','?','-','?','?','IN07'],
    ['M','X','?','?','?','?','X','?','?','?','IN08'],
    ['M','X','?','?','?','?','-','?','?','?','IN09'],
    ['M','X','?','?','?','?','?','?','?','?','IN10'],
    ['M','X','?','?','?','?','?','X','?','?','IN12'],
    ['M','X','?','?','?','?','?','-','?','?','IN13'],
    ['M','X','?','?','?','?','X','?','?','?','IN14'],
    ['M','X','?','?','?','?','-','?','?','?','IN16'],
    ['M','X','?','?','?','?','?','?','?','?','IN19'],
    ['M','X','?','?','?','?','?','X','?','?','RO01'],
    ['M','-','X','?','?','?','?','-','?','?','BE01'],
    ['M','-','X','?','?','?','X','?','?','?','BE04'],
    ['M','-','X','?','?','?','-','?','?','?','BR06'],
    ['M','-','X','?','?','?','?','?','?','?','IM02'],
    ['M','-','X','?','?','?','?','X','?','?','IM03'],
    ['M','-','X','?','?','?','?','-','?','?','IM06'],
    ['M','-','X','?','?','?','X','?','?','?','IM09'],
    ['M','-','X','?','?','?','-','?','?','?','IN12'],
    ['M','-','X','?','?','?','?','?','?','?','IN13'],
    ['M','-','X','?','?','?','?','X','?','?','RO03'],
    ['M','-','X','?','?','?','?','-','?','?','RO04'],
    ['M','-','-','?','?','?','X','-','?','?','BE04'],
    ['M','-','-','?','?','?','-','?','?','?','BE01'],
    ['M','-','-','?','?','?','?','?','?','?','BR06'],
    ['M','-','-','?','?','?','?','X','?','?','IM02'],
    ['M','-','-','?','?','?','?','-','?','?','IN04'],
    ['M','-','-','?','?','?','X','-','?','?','IN05'],
    ['M','-','-','?','?','?','-','?','?','?','IN06'],
    ['M','-','-','?','?','?','?','?','?','?','IN07'],
    ['M','-','-','?','?','?','?','X','?','?','IN08'],
    ['M','-','-','?','?','?','?','-','?','?','IN09'],
    ['M','-','-','?','?','?','X','-','?','?','IN10'],
    ['M','-','-','?','?','?','-','?','?','?','IN11'],
    ['M','-','-','?','?','?','?','?','?','?','IN12'],
    ['M','-','-','?','?','?','?','X','?','?','IN13'],
    ['M','-','-','?','?','?','?','-','?','?','IN14'],
    ['M','-','-','?','?','?','X','-','?','?','IN17'],
    ['M','-','-','?','?','?','-','?','?','?','IN18'],
    ['M','-','-','?','?','?','?','?','?','?','RO04'],
    ['M','-','-','?','?','?','?','X','?','?','RO07'],
    ['M','-','-','?','?','?','?','-','?','?','BE02'],
    ['M','-','-','?','?','?','X','-','?','?','BE03'],
    ['M','-','-','?','?','?','-','?','?','?','BE06'],
    ['M','-','-','?','?','X','?','?','?','?','IN15'],
    ['M','-','-','?','?','-','?','X','?','?','IN16'],
    ['M','-','-','-','-','-','X','?','?','?','BE03'],
    ['M','?','?','?','?','?','?','X','?','?','IM03'],
    ['M','?','?','?','?','?','?','X','?','?','IM04'],
    ['M','?','?','?','?','?','?','X','?','?','IM06'],
    ['M','?','?','?','?','?','?','?','X','?','BE05'],
    ['M','?','?','?','?','?','?','?','X','?','BR02'],
    ['M','?','?','?','?','?','?','?','X','?','BR03'],
    ['M','?','?','?','?','?','?','?','X','?','BR04'],
    ['M','?','?','?','?','?','?','?','X','?','BR05'],
    ['M','?','?','?','?','?','?','?','X','?','BR06'],
    ['M','?','?','?','?','?','?','?','X','?','BR07'],
    ['M','?','?','?','?','?','?','?','X','?','BR08'],
    ['M','?','?','?','?','?','?','?','X','?','BR09'],
    ['M','?','?','?','?','?','?','?','X','?','IM02'],
    ['M','?','?','?','?','?','?','?','X','?','IM04'],
    ['M','?','?','?','?','?','?','?','X','?','IM06'],
    ['M','?','?','?','?','?','?','?','X','?','IM07'],
    ['M','?','?','?','?','?','?','?','X','?','IM09'],
    ['M','?','?','?','?','?','?','?','?','X','BE06'],
    ['M','?','?','?','?','?','?','?','?','X','IN07'],
    ['M','?','?','?','?','?','?','?','?','X','IN08'],
    ['M','?','?','?','?','?','?','?','?','X','IN09'],
    ['M','?','?','?','?','?','?','?','?','X','IN10'],
    ]

class EsfPatterns(object):
    """Implements the fucntionality to insert ESF patterns in the database."""

    def insert(self, patterns):
        """Insert the specified ESF patterns in the database.

        Parameter ``patterns`` is a list of patterns, where each pattern is
        specified by a list of 10 strings. Let p be such a pattern, then

          - p[0] specifies the code of the WatertypeGroup,
          - p[i], where 0 < i < 10, is a string that specifies whether ESF i
            should be critical (value 'X'), not critical (value '-') or does
            not care (value '?'), and
          - p[10] specifies the code of the MeasureType.

        """
        for pattern in patterns:
            watertype_group_code = pattern[0]
            string_pattern = ''.join(pattern[1:10])

            esf_pattern, created = \
                EsfPattern.objects.get_or_create(watertype_group__code=watertype_group_code,
                                                 pattern=string_pattern)

            watertype_group = WatertypeGroup.objects.get(code=watertype_group_code)
            esf_pattern.watertype_group = watertype_group

            # Before we can use the many-to-many relationship of the ESF
            # pattern, the pattern must have a primary key. So we save the
            # pattern to generate that key.
            esf_pattern.save()

            measure_type = MeasureType.objects.get(code=pattern[10])
            esf_pattern.measure_types.add(measure_type)

            esf_pattern.save()

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
       EsfPatterns().insert(PATTERNS)

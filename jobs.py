#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json


def get(str):
    """
    Parse json string.
    If successfully return dict else None.
    """
    try:
        raw = json.loads(str)
        ids = [job['id'] for job in raw['jobs']]
        pag = raw['paging']
        ofs = int(pag['offset']) + int(pag['count'])
        return {'PAGE_OFFSET': ofs, 'JOB_IDS': ids}
    except:
        pass
    return None
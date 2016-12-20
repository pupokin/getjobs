#!/usr/bin/env python
# -*- coding: utf-8 -*-


import jobs
import unittest


class TestJobsMethods(unittest.TestCase):
    def test_get(self):
        str = r"""
{
    "jobs": [
        {
            "id": "~01c1ea2a6f015b04ed",
            "title": "Urgent: Need someone to make content changes to Wordpress/wishlist member",
            "snippet": "Looking for someone who can work right now. \n\nNeed to Make changes to the content on two of my pages in wordpress. \n\nI have to member levels that have the same home page. But I need to make changes to the content in this area example:\n\nhttp://screencast.com/t/ZNyqrCly\n\nYou must be able to work on this immediately. I don't have an edit button on those pages to do it myself and I don't trust myself on the back-end system.\n\nOnce hired you must be able to do this and complete within 30mins (it should take you less time). It's almost 10a Est and would need this done before 11a EST.",
            "category2": "Web, Mobile & Software Dev",
            "subcategory2": "Web Development",
            "skills": [
                "wordpress"
            ],
            "job_type": "Fixed",
            "budget": 25,
            "duration": null,
            "workload": null,
            "job_status": "Completed",
            "date_created": "2016-12-17T14:53:47+0000",
            "url": "http://www.upwork.com/jobs/~01c1ea2a6f015b04ed",
            "client": {
                "country": "United States",
                "feedback": 4.9559904635,
                "reviews_count": 85,
                "jobs_posted": 234,
                "past_hires": 158,
                "payment_verification_status": null
            }
        },
        {
            "id": "~01bc41dfdf2a547e00",
            "title": "Install Plugin in WordPress Page",
            "snippet": "Hi - I need help setting up my WordPress page and installing a plug-in. Can you help?\r\n\r\nThank you.",
            "category2": "Web, Mobile & Software Dev",
            "subcategory2": "Web Development",
            "skills": [],
            "job_type": "Fixed",
            "budget": 30,
            "duration": null,
            "workload": null,
            "job_status": "Completed",
            "date_created": "2016-12-15T10:43:27+0000",
            "url": "http://www.upwork.com/jobs/~01bc41dfdf2a547e00",
            "client": {
                "country": "United States",
                "feedback": 0,
                "reviews_count": 0,
                "jobs_posted": 1,
                "past_hires": 2,
                "payment_verification_status": null
            }
        },
        {
            "id": "~017d11c03e47d62489",
            "title": "WordPress Security",
            "snippet": "A new client has an infected website, our job is simple: Clean WordPress website from infection and secure it for the future.\n\nTime-frame: 2 days \n\nWe will provide you with access to the server where the website is installed. ",
            "category2": "Web, Mobile & Software Dev",
            "subcategory2": "Web Development",
            "skills": [
                "html",
                "website-development",
                "wordpress"
            ],
            "job_type": "Hourly",
            "budget": 0,
            "duration": "Less than 1 week",
            "workload": "Less than 10 hrs/week",
            "job_status": "Completed",
            "date_created": "2016-12-04T23:12:17+0000",
            "url": "http://www.upwork.com/jobs/~017d11c03e47d62489",
            "client": {
                "country": "United States",
                "feedback": 4.8815090921,
                "reviews_count": 12,
                "jobs_posted": 15,
                "past_hires": 15,
                "payment_verification_status": null
            }
        }
    ],
    "paging": {
        "offset": 0,
        "count": 10,
        "total": 147198
    }
}
        """
        res = {'PAGE_OFFSET': 10, 'JOB_IDS': ['~01c1ea2a6f015b04ed', '~01bc41dfdf2a547e00', '~017d11c03e47d62489']}
        self.assertEqual(jobs.get(str), res)


if __name__ == '__main__':
    unittest.main()
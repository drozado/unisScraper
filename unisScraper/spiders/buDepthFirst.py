# -*- coding: utf8 -*-
import scrapy
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join


from unisScraper.items import unisScraperItem


class ToScrapeSpiderXPath(CrawlSpider):

	name = 'BuDepthFirst'
	# allowed_domains = ['drfteaching.wordpress.com']  # The bounds of the project
	# start_urls = ['https://drfteaching.wordpress.com']  # The starting page for the project
	#allowed_domains = ['github.com', 'accessibilitysoftwarehub.github.io']  # The bounds of the project
	#start_urls = ['https://accessibilitysoftwarehub.github.io']  # The starting page for the project

	allowed_domains = ['bu.edu']  # The bounds of the project
	start_urls = ['http://bu.edu']  # The starting page for the project
	depth_limit = 3

	custom_settings = {
					   'LOG_FILE': r"I:\COURSES\EAD\AITEIT3\BITY3\IN700001 Project\NLP\david\BuDepthFirstDepthLimit3.log",
					   'LOG_ENABLED': True,
					   'LOG_STDOUT': False,
					   'LOG_LEVEL' : 'DEBUG',
					   'DEPTH_LIMIT': depth_limit,
					   'FEED_URI': r'file:///I:/COURSES/EAD/AITEIT3/BITY3/IN700001 Project/NLP/david/%(name)sDepthLimit%(depth_limit)s.csv',
					   'FEED_FORMAT': 'csv',
					   'AUTOTHROTTLE_ENABLED': True
					   }

	rules = [#The callback function cannot be parse
		Rule(LinkExtractor(),callback='parse_item',follow=True),
	]

	# Runs once for each webpage:
	def parse_item(self, response):
		#print("Existing settings: %s" % self.settings.attributes.keys())
		#self.logger.info('A response from %s just arrived!', response.url)
		self.logger.info("Existing settings: %s" % self.settings.attributes['LOG_FILE'])

        # Create the loader using the response
		l = ItemLoader(item=unisScraperItem(), response=response)


		l.add_value('url', response.url)

		l.add_xpath('text', '//p/text()',MapCompose(str.strip),Join())

		return l.load_item()


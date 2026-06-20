from pep_parse.constants import RESULTS_DIR_NAME, PEP_FILENAME


BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = False

FEEDS = {
    f'{RESULTS_DIR_NAME}/{PEP_FILENAME}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'encoding': 'utf-8',
        'overwrite': True,
    },
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}

FEED_EXPORT_ENCODING = "utf-8"
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
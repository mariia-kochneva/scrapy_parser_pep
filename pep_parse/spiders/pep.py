import scrapy
import re
from scrapy.http import Response

from pep_parse.items import PepParseItem
from pep_parse.constants import EXPECTED_STATUS, PEP_URL


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = [PEP_URL]

    def parse(self, response: Response):
        rows = response.css('table.pep-zero-table tbody tr')
        self.logger.info(f'Найдено строк в таблице: {len(rows)}')
        for row in rows:
            number_cell = row.css('td:nth-child(2) a')
            pep_num = number_cell.css('::text').get()
            if not pep_num or not pep_num.isdigit() or pep_num == '0':
                continue
            status_cell = row.css('td:nth-child(1)::text').get()
            expected_status = self._get_expected_status(status_cell)
            pep_url = response.urljoin(number_cell.attrib['href'])
            yield scrapy.Request(
                url=pep_url,
                callback=self.parse_pep,
                meta={
                    'pep_number': int(pep_num),
                    'expected_status': expected_status
                }
            )

    def parse_pep(self, response: Response):
        number = response.meta.get('pep_number')
        name = ''
        title = response.css('h1::text').get()
        if title:
            name = re.sub(r'PEP\s+\d+\s*[–-]\s*', '', title).strip()
            if name == 'Python Enhancement Proposals' or not name:
                title_tag = response.css('title::text').get()
                if title_tag:
                    name = (
                        re.sub(r'PEP\s+\d+\s*[–-]\s*', '', title_tag).strip()
                    )
                    name = re.sub(r'\s*\|.*$', '', name).strip()
                else:
                    name = title.strip()
        actual_status = self._get_actual_status(response)
        yield PepParseItem(
            number=number,
            name=name,
            status=actual_status,
        )

    def _get_expected_status(self, status_text: str) -> tuple:
        if not status_text:
            return EXPECTED_STATUS.get('', ('Unknown',))
        status_letter = (
            status_text[1] if len(status_text) > 1 else status_text[0]
        )
        return EXPECTED_STATUS.get(status_letter, ('Unknown',))

    def _get_actual_status(self, response: Response) -> str:
        status = response.xpath(
            '//dd[contains(@class, "field-even")]/abbr/text()'
        ).get()
        if not status:
            status = response.xpath(
                '//dd[contains(@class, "field-odd")]/abbr/text()'
            ).get()
        return status.strip() if status else 'Unknown'

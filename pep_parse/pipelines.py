from datetime import datetime
from pathlib import Path


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_counts = {}
        self.pep_items = []

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            self.status_counts[status] = self.status_counts.get(status, 0) + 1
        self.pep_items.append(item)
        return item

    def close_spider(self, spider):
        results_dir = Path('results')
        results_dir.mkdir(exist_ok=True)
        now = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        pep_filename = results_dir / f'pep_{now}.csv'
        with open(pep_filename, 'w', encoding='utf-8') as f:
            f.write('number,name,status\n')
            for item in self.pep_items:
                f.write(f"{item['number']},{item['name']},{item['status']}\n")
        summary_filename = results_dir / f'status_summary_{now}.csv'
        total = sum(self.status_counts.values())
        with open(summary_filename, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in sorted(self.status_counts.items()):
                f.write(f'{status},{count}\n')
            f.write(f'Total,{total}\n')
        spider.logger.info(
            f'Файлы сохранены: {pep_filename}, {summary_filename}'
        )

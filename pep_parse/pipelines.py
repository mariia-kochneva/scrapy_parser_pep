from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'results'


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_counts = {}

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            self.status_counts[status] = self.status_counts.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        results_dir = RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        summary_filename = results_dir / f'status_summary_{now}.csv'
        total = sum(self.status_counts.values())
        with open(summary_filename, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in sorted(self.status_counts.items()):
                f.write(f'{status},{count}\n')
            f.write(f'Total,{total}\n')
        spider.logger.info(f'Сводка сохранена в {summary_filename}')

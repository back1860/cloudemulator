import sys

import config
from common import log as logging
import service


def rest():
    config.parse_args(sys.argv)
    logging.setup("cloudemulator")

    launcher = service.process_launcher()

    server = service.WSGIService('rest', use_ssl=False,
                                 max_url_len=16384)
    launcher.launch_service(server, workers=server.workers or 1)
    launcher.wait()

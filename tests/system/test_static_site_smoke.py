import contextlib
import http.server
import pathlib
import socket
import socketserver
import threading
import unittest
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[2]


def free_port():
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        return


class StaticSiteSystemTests(unittest.TestCase):
    def test_static_site_serves_html_css_and_js(self):
        port = free_port()
        handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(ROOT), **kwargs)
        with socketserver.TCPServer(("127.0.0.1", port), handler) as server:
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                for path, expected in [
                    ("/", "Rubik Structural Studio"),
                    ("/styles.css", "version-footer"),
                    ("/app.js", "APP_METADATA"),
                ]:
                    with urllib.request.urlopen(f"http://127.0.0.1:{port}{path}", timeout=5) as response:
                        body = response.read().decode("utf-8")
                        status = response.status
                    self.assertEqual(status, 200)
                    self.assertIn(expected, body)
            finally:
                server.shutdown()
                thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()


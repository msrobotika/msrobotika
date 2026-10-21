# SPDX-License-Identifier: MIT
"""Browser integration: real server, original frontend and synthetic test plate."""
from pathlib import Path
import subprocess
import sys
import unittest
import http.client
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'docs'/'screenshots'
class BrowserSmoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proc=subprocess.Popen([sys.executable,'-u','serve.py','--no-browser'],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        cls.proc.stdout.readline();cls.url=cls.proc.stdout.readline().strip()
        assert cls.url.startswith('http://127.0.0.1:'),cls.url
        cls.pw=sync_playwright().start()
        cls.browser=cls.pw.chromium.launch(executable_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None,headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.pw.stop();cls.proc.terminate();cls.proc.wait(timeout=8);cls.proc.stdout.close()
    @staticmethod
    def inline_app():
        # Chromium in this sandbox blocks localhost navigation by administrator
        # policy. The genuine HTML, CSS and JS are embedded unchanged in a
        # sandboxed about:blank test page, not mocked; the Python HTTP server
        # is tested separately via an actual request.
        html=(ROOT/'index.html').read_text(encoding='utf-8')
        html=html.replace('<link rel="stylesheet" href="/src/style.css">',
            '<style>'+(ROOT/'src/style.css').read_text(encoding='utf-8')+'</style>')
        html=html.replace('<script src="/src/vision-core.js" defer></script>', '')
        html=html.replace('<script src="/src/app.js" defer></script>', '')
        html=html.replace('</body>',
            '<script>'+(ROOT/'src/vision-core.js').read_text(encoding='utf-8')+'</script>'+
            '<script>'+(ROOT/'src/app.js').read_text(encoding='utf-8')+'</script></body>')
        html=html.replace('<link rel="icon" href="/favicon.svg">','')
        return html

    def test_server_is_local_and_no_upload(self):
        parsed=urlsplit(self.url)
        conn=http.client.HTTPConnection(parsed.hostname,parsed.port,timeout=5)
        conn.request('GET','/')
        r=conn.getresponse();body=r.read()
        self.assertEqual(r.status,200)
        self.assertIn(b'AB-Vision Inspector',body)
        self.assertIn('frame-ancestors',r.getheader('Content-Security-Policy'))
        conn.request('POST','/',body=b'secret-image')
        self.assertEqual(conn.getresponse().status,405)
        conn.close()

    def test_portable_html_without_network(self):
        page=self.browser.new_page(viewport={'width':1280,'height':840})
        requests=[]
        page.on('request',lambda request: requests.append(request.url))
        html=(ROOT/'AB-Vision-Inspector-PORTABLE.html').read_text(encoding='utf-8')
        page.set_content(html,wait_until='load')
        page.locator('#analyze').click()
        page.wait_for_function("() => document.querySelector('#verdict').textContent==='NOK'")
        self.assertEqual(page.locator('#defects').inner_text(),'4')
        self.assertFalse(requests,'El portable no debe descargar librerías ni enviar datos')
        page.close()

    def test_audit_fail_closed_and_screenshot(self):
        """Las medidas requieren patrón visible en cada fotograma, no solo al inicio."""
        OUT.mkdir(parents=True,exist_ok=True)
        page=self.browser.new_page(viewport={'width':1440,'height':950},device_scale_factor=1)
        errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
        page.set_content(self.inline_app(),wait_until='load',timeout=25000)
        page.locator('#reference-mm').fill('100')
        page.locator('#nominal-width').fill('111.46')
        page.locator('#nominal-height').fill('53.65')
        page.locator('#dimension-tolerance').fill('2')
        page.locator('#mark-scale').click()
        for x,y in ((160,667),(1120,667)):
            page.evaluate("""([x,y]) => {
              const el=document.querySelector('#overlay'),r=el.getBoundingClientRect();
              el.dispatchEvent(new PointerEvent('pointerdown',{
                bubbles:true,pointerId:3,
                clientX:r.x+x*r.width/el.width,clientY:r.y+y*r.height/el.height
              }));
            }""",[x,y])
        self.assertIn('CALIBRADA Y AUDITADA',page.locator('#calibration-status').inner_text())
        page.locator('#analyze').click()
        self.assertEqual(page.locator('#measured-size').inner_text(),'111.45 × 53.64')
        self.assertIn('VERIFICADA',page.locator('#audit-status').inner_text())
        page.screenshot(path=str(OUT/'vision-calibracion-auditada.png'),full_page=True,animations='disabled')
        page.evaluate("""() => { const ctx=document.querySelector('#source').getContext('2d');
          ctx.fillStyle='#345963';ctx.fillRect(147,654,28,29); }""")
        page.locator('#analyze').click()
        self.assertIn('NO VALIDADA',page.locator('#audit-status').inner_text())
        self.assertEqual(page.locator('#verdict').inner_text(),'SIN MEDICIÓN')
        self.assertEqual(page.locator('#measured-size').inner_text(),'INVÁLIDA')
        page.screenshot(path=str(OUT/'vision-auditoria-bloqueada.png'),full_page=True,animations='disabled')
        self.assertEqual(errors,[])
        page.close()

    def test_ui_and_screenshots(self):
        OUT.mkdir(parents=True,exist_ok=True)
        page=self.browser.new_page(viewport={'width':1440,'height':980},device_scale_factor=1,accept_downloads=True)
        errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
        responses=[];page.on('response',lambda r: responses.append((r.url,r.status)))
        page.set_content(self.inline_app(),wait_until='load',timeout=25000)
        self.assertEqual(page.locator('#source-label').inner_text(),'Muestra técnica sintética · chapa con defectos')
        page.locator('#analyze').click()
        page.wait_for_function("() => document.querySelector('#verdict').textContent === 'NOK'",timeout=25000)
        amount=int(page.locator('#defects').inner_text())
        self.assertEqual(amount,4,'La demo debe producir cuatro manchas separadas')
        self.assertIn('%',page.locator('#coverage').inner_text())
        self.assertEqual(page.locator('#count').inner_text(),'1')
        page.screenshot(path=str(OUT/'vision-dashboard.png'),full_page=True,animations='disabled')
        page.locator('#max-defects').fill('5');page.locator('#analyze').click()
        self.assertEqual(page.locator('#verdict').inner_text(),'OK')
        page.locator('#mode').select_option('reference');page.locator('#set-reference').click();page.locator('#analyze').click()
        self.assertEqual(page.locator('#defects').inner_text(),'0')
        page.locator('#export-csv').click()
        with page.expect_download() as download:
            page.locator('#export-json').click()
        self.assertTrue(download.value.suggested_filename.endswith('.json'))
        self.assertEqual(errors,[])
        self.assertFalse(any(status>=400 for url,status in responses if url.startswith(self.url)))
        page.close()
        mobile=self.browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
        mobile.set_content(self.inline_app(),wait_until='load',timeout=25000)
        mobile.locator('#analyze').click()
        mobile.wait_for_function("() => document.querySelector('#verdict').textContent === 'NOK'",timeout=25000)
        mobile.screenshot(path=str(OUT/'vision-mobile.png'),full_page=True,animations='disabled')
        self.assertFalse(mobile.evaluate('document.documentElement.scrollWidth > innerWidth'))
        mobile.close()

// Florida 500 – offline cache. index.html/data.js はネット優先（更新を拾う）、それ以外はキャッシュ優先。
const CACHE = 'florida500-v7';
const ASSETS = ['./', './index.html', './data.js', './dialog.js', './manifest.webmanifest', './icon-180.png', './icon-512.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;
  const networkFirst = /index\.html$|data\.js$|\/$/.test(url.pathname);
  e.respondWith(
    networkFirst
      ? fetch(e.request).then(r => { const c = r.clone(); caches.open(CACHE).then(cache => cache.put(e.request, c)); return r; }).catch(() => caches.match(e.request))
      : caches.match(e.request).then(r => r || fetch(e.request).then(r2 => { const c = r2.clone(); caches.open(CACHE).then(cache => cache.put(e.request, c)); return r2; }))
  );
});

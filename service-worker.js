const cacheName = 'ai-universe-cache-v1';
const staticAssets = [
  './',
  './index.html',
  './desktop.html',
  './mobile.html',
  './style.css',
  './script.js',
  './manifest.json',
  './simple ai pulse.json',
  './simple ai pulse.png'
];

self.addEventListener('install', async event => {
  const cache = await caches.open(cacheName);
  await cache.addAll(staticAssets);
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});

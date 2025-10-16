self.addEventListener('install', function (e) {
    e.waitUntil(
        caches.open('projectsite-cache-v1').then(function (cache) {
            return cache.addAll([
                '/',
                '/static/css/plugins/bootstrap.min.css',
                '/static/js/plugins/bootstrap.min.js',
                '/static/js/component.js',
                '/static/js/pcoded.js',
                ''
            ]);
        })
    );
});
self.addEventListener('fetch', function (e) {
    e.respondWith(
        caches.match(e.request).then(function (response) {
            return response || fetch(e.request);
        })
    );
});
var serviceWorkerPath = "/charcha-serviceworker.js";
var charchaServiceWorker = registerServiceWorker(serviceWorkerPath);
function registerServiceWorker(serviceWorkerPath){
   if('serviceWorker' in navigator){
     navigator.serviceWorker
       .register(serviceWorkerPath)
         .then(
           function(reg){
             console.log('charcha service worker registered');
           }
         ).catch(function(error){
           console.log(error)
         });
   }
}

var cacheName = 'charcha';
var filesToCache = [
'/',
];
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(cacheName).then(function(cache) {
      return cache.addAll(filesToCache);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        if (response) {
          return response;
        }
        var fetchRequest = event.request.clone();
        return fetch(fetchRequest).then(
          function(response) {
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            var responseToCache = response.clone();
            caches.open(cacheName)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });
            return response;
          }
        );
      })
    );
});

self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(keyList) {
      return Promise.all(keyList.map(function(key) {
        if (key !== cacheName) {
          return caches.delete(key);
        }
      }));
    })
  );
});
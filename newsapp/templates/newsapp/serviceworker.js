self.addEventListener("install", function(event) {
  event.waitUntil(preLoad());
});

var preLoad = function(){
  console.log("Installing web app");
  return caches.open("/").then(function(cache) {
    console.log("caching index and important routes");
    return cache.addAll(["/"]);
  });
};

self.addEventListener("fetch", function(event) {
  event.respondWith(checkResponse(event.request).catch(function() {
    return returnFromCache(event.request);
  }));
  event.waitUntil(addToCache(event.request));
});

var checkResponse = function(request){
  return new Promise(function(fulfill, reject) {
    fetch(request).then(function(response){
      if(response.status !== 404) {
        fulfill(response);
      } else {
        reject();
      }
    }, reject);
  });
};

var addToCache = function(request){
  return caches.open("/").then(function (cache) {
    return fetch(request).then(function (response) {
      console.log(response.url + " was cached");
      return cache.put(request, response);
    });
  });
};

var returnFromCache = function(request){
  return caches.open("/").then(function (cache) {
    return cache.match(request).then(function (matching) {
     if(!matching || matching.status == 404) {
       return cache.match("/");
     } else {
       return matching;
     }
    });
  });
};

// Web Push Notifications
// Register event listener for the 'push' event.
self.addEventListener('push', function (event) {
  // Retrieve the textual payload from event.data (a PushMessageData object).
  // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
  // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.
  const eventInfo = event.data.text();
  const data = JSON.parse(eventInfo);
  const head = data.head || 'New Notification 🕺🕺';
  const body = data.body || 'This is default content. Your notification didn\'t have one 🙄🙄';

  // Keep the service worker alive until the notification is created.
  event.waitUntil(
      self.registration.showNotification(head, {
          body: body,
          icon: 'https://i.imgur.com/MZM3K5w.png'
      })
  );
});
